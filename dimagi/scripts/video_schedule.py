import settings
from django.core.management import setup_environ
setup_environ(settings)
from dashboard.models import *
import xlrd

def get_video_schedule():
    book = xlrd.open_workbook("bihar_video_schedule.xls", formatting_info=1)
    sheets = book.sheet_names()
    sheet = book.sheet_by_index(0)   # using the first sheet
    dates = ['2013-01-01','2013-01-16','2013-02-01','2013-02-16','2013-03-01','2013-03-16','2013-04-01','2013-04-16','2013-05-01','2013-05-16','2013-06-01','2013-06-16',
             '2013-07-01','2013-07-16','2013-08-01','2013-08-16','2013-09-01','2013-09-16','2013-10-01','2013-10-16','2013-11-01','2013-11-16','2013-12-01','2013-12-16','2013-12-31']
    row = 2
    vid_dict = []
    vid_list = []
    print sheet.nrows
    while( row < sheet.nrows):
        col = 0    
        vid_id = Video.objects.filter(title = sheet.cell(row, col).value).values_list('id', flat = True)
        col += 1
        if len(vid_id) == 1 :
            vid_list.append(vid_id[0])
            while( col < sheet.ncols ):
                format_info = sheet.cell_xf_index(row, col)
                format_info = book.xf_list[format_info]
                bg_color = format_info.background.pattern_colour_index
                if bg_color == 13:
                    low = col
                    while( col < sheet.ncols):
                        format_info = sheet.cell_xf_index(row, col)
                        format_info = book.xf_list[format_info]
                        bg_color = format_info.background.pattern_colour_index
                        if bg_color == 13:
                            col += 1
                        else:
                            high = col
                            vid_dict.append({'id': vid_id[0],
                                            'low_val': dates[low-2],
                                            'high_val': dates[high-2] })
                            break                  
                col += 1 
        row += 1
    return vid_dict, vid_list