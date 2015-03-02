__author__ = 'Lokesh'

import os.path
from configuration import tableDictionary, whereDictionary, selectDictionary, groupbyDictionary, categoryDictionary
import pandas as pd
import MySQLdb
import pandas.io.sql as psql
import csv
import dg.settings
from static_queries import static_query

class data_lib():
    Dict = {}
    lookup_matrix = {}

    def read_lookup_csv(self):
        # file_data = csv.reader(open('C:/Users/Lokesh/Documents/dg/dg/media/raw_data_analytics/data_analytics.csv'))
        file_data = csv.reader(open(os.path.join(dg.settings.MEDIA_ROOT + r'/raw_data_analytics/data_analytics.csv')))
        headers = next(file_data)
        headers.remove('')
        matrix = {}
        for row in file_data:
            sub_matrix = {}
            for i in range(0, len(headers)):
                sub_matrix[headers[i]] = []
                temp = row[i + 1].split('$')
                for t in temp:
                    if '&' in t:
                        andtemp = t.split('&')
                        for vl in andtemp:
                            sub_matrix[headers[i]].append(tuple(vl.split('#')))
                    else:
                        sub_matrix[headers[i]].append(tuple(t.split('#')))
            matrix[row[0]] = sub_matrix
        return matrix

    # Function to check validity of the partition field inputs by user by comparing with the generalPartitionList
    def check_partitionfield_validity(self, partitionField):
    #    print partitionField
        if set(partitionField.keys()).issubset(tableDictionary.keys()):
            return True
        else:
            return False


    # Function to check validity of the value field inputs by user by comparing with the generalValueList

    def check_valuefield_validity(self, valueField):
        if set(valueField.keys()).issubset(tableDictionary.keys()):
            return True
        else:
            return False


    def handle_controller(self, args, options):
    # Accepts options i.e. dictionary of dictionary e.g. {'partition':{'partner':'','state',''},'value':{'nScreening':True,'nAdoption':true}}
    # This function is responsible to call function for checking validity of input and functions to make dataframes according to the inputs

    #    print options['partition']
    #    print options['value']
        self.lookup_matrix = self.read_lookup_csv()
        relevantPartitionDictionary = {}
        relevantValueDictionary = {}
        # --- checking validity of the partition fields and value fields entered by user ---
        print static_query['numAdoption']
        if self.check_partitionfield_validity(options['partition']):
    #        print "valid input for partition fields"
            for item in options['partition']:
                if options['partition'][item] != False:
                    relevantPartitionDictionary[item] = options['partition'][item]
        else:
            print "Warning - Invalid input for partition fields"

        if self.check_valuefield_validity(options['value']):
    #       print "valid input for value fields"
            for item in options['value']:
                if item =='list' and options['value']['list']!=False:
                    relevantValueDictionary[options['value'][item]] = True
    #                print item
    #                print options['value'][item]
                    relevantPartitionDictionary[categoryDictionary['partitionCumValues'][options['value'][item]]] = False
                    del relevantPartitionDictionary[categoryDictionary['partitionCumValues'][options['value'][item]]]
                if options['value'][item] != False and item!='list':
                    relevantValueDictionary[item] = options['value'][item]
        else:
            print "Warning - Invalid input for Value fields"

        final_df = pd.DataFrame()

    #    print "%%%%%%%%%%%%%%%%% Relevant Partition Dictionary %%%%%%%%%%%%%%%%%%" + str(relevantPartitionDictionary)
    #    print "################# Relevant Value Dictionary ##################" + str(relevantValueDictionary)

        for input in relevantValueDictionary:
    #        print queryComponents
    #        print "----------------------------------Full SQL Query---------------------------"
            query = self.getRequiredTables(relevantPartitionDictionary, input, args, self.lookup_matrix)
    #        print query
    #        print "-------------------------------Result--------------------------------"
            df = self.runQuery(query)
            if final_df.empty:
                final_df = df
            else:
                how=''
                if len(final_df)>len(df):
                    how = 'left'
                else:
                    how='right'
    #            print how
                final_df = pd.merge(final_df, df, how=how)
    #        print df
            # /home/ubuntu/code/dg_coco_test/dg/
        return final_df


    def getRequiredTables(self, partitionDict, valueDictElement, args, lookup_matrix):
        query_to_run = ''
        if valueDictElement == 'numAdoption' or valueDictElement == 'attendance':
            select_from_query_to_run = self.getStaticQuery(partitionDict,valueDictElement,args).split('FROM')
            whereResult = self.getWhereComponent(partitionDict, valueDictElement, self.Dict, args, lookup_matrix)
            groupbyResult = self.getGroupByComponent(partitionDict, valueDictElement)
            query_to_run = self.makeSQLquery(select_from_query_to_run[0].replace('SELECT',''),select_from_query_to_run[1],whereResult,groupbyResult)
        else:
            self.Dict.clear()
            selectResult = self.getSelectComponent(partitionDict, valueDictElement)
            fromResult = self.getFromComponent(partitionDict, valueDictElement, lookup_matrix)
            whereResult = self.getWhereComponent(partitionDict, valueDictElement, self.Dict, args, lookup_matrix)
            groupbyResult = self.getGroupByComponent(partitionDict, valueDictElement)
        #    print "----------------------------------SELECT PART------------------------------"
        #    print selectResult
        #    print "----------------------------------FROM PART--------------------------------"
        #    print fromResult
        #    print "----------------------------------WHERE PART-------------------------------"
        #    print whereResult
        #    print "---------------------------------GROUP_BY PART----------------------------"
        #    print groupbyResult
            query_to_run = self.makeSQLquery(selectResult, fromResult, whereResult, groupbyResult)
        return (query_to_run)


    def makeSQLquery(self, select_msg, from_msg, where_msg, groupby_msg):
        query = 'SELECT ' + str(select_msg) + ' FROM ' + str(from_msg) + ' WHERE ' + str(
            where_msg) + ' GROUP BY ' + str(groupby_msg)
        return query


    def getSelectComponent(self, partitionElements, valueElement):
        selectComponentList = []
        for items in partitionElements:
            for i in selectDictionary[items]:
                if (selectDictionary[items][i] == True):
                    selectComponentList.append(tableDictionary[items] + '.' + i + ' AS ' + items)
    #    print selectComponentList
        for i in selectDictionary[valueElement]:
            if (selectDictionary[valueElement][i] == True):
                if "count" in i:
                    selectComponentList.append(
                        i.replace('count(', 'count(distinct ' + str(tableDictionary[valueElement]) + '.') + ' AS ' + valueElement)
                else:
                    selectComponentList.append(str(tableDictionary[valueElement]) + '.' + i + ' AS ' + valueElement)
        return ','.join(selectComponentList)


    # Function to make tables by recursive calls for tables.
    def makeJoinTable(self, sourceTable, destinationTable, lookup_matrix, occuredTables, Dict):
        if (sourceTable not in occuredTables):
            for i in lookup_matrix[sourceTable][destinationTable]:
                if (i[2] == 'self'):
    #                print 'SELF'
                    return
                elif (i[2] == 'direct'):
    #                print 'DIRECT'
                    if (destinationTable not in occuredTables):
                        occuredTables.append(destinationTable)
                    if (sourceTable in Dict.keys()):
                        if (destinationTable not in Dict[sourceTable]):
                            Dict[sourceTable].append(destinationTable)
                    else:
                        Dict[sourceTable] = [destinationTable]
                    occuredTables.append(sourceTable)
                    return
                else:
                    if (sourceTable in Dict.keys()):
                        Dict[sourceTable].append(i[2])
                    else:
                        Dict[sourceTable] = [i[2]]
                    occuredTables.append(sourceTable)
                    self.makeJoinTable(i[2], destinationTable, lookup_matrix, occuredTables, Dict)
        else:
            return


        # Function to make FROM component of the sql query
    def getFromComponent(self, partitionElements, valueElement, lookup_matrix):
        partitionTables = []
        for i in partitionElements:
            if (i in categoryDictionary['geographies']):
                partitionTables.insert(0, tableDictionary[i])
            else:
                partitionTables.append(tableDictionary[i])
        majorTablesList = []
        tablesOccuredList = []
        for index, table in enumerate(partitionTables):
            minorTablePath = []
            if table not in self.Dict.keys():
                self.Dict[table] = []
            if (table not in majorTablesList):
                minorTablePath.append(table)
                self.makeJoinTable(table, tableDictionary[valueElement], lookup_matrix, tablesOccuredList, self.Dict)
        majorTablesList = tablesOccuredList
        return ' , '.join(majorTablesList)


    # Function to make whereComponent of the query
    def getWhereComponent(self, partitionElements, valueElement, Dictionary, args, lookup_matrix):
        whereString = '1=1'
        whereComponentList = [whereString]
    #    print lookup_matrix
    #    print "###########Dictionary is:##################" + str(Dictionary)
        for items in partitionElements:
            if partitionElements[items] != True:
                whereComponentList.append(
                    tableDictionary[items] + '.' + whereDictionary[items] + '=' + partitionElements[items])
        for i in Dictionary:
            for j in Dictionary[i]:
                for k in range(0,len(lookup_matrix[i][j])):
    #                print str(i) + '.' + str(lookup_matrix[i][j][k][0]) + '=' + str(j) + '.' + str(lookup_matrix[i][j][k][1])
                    whereComponentList.append(str(i) + '.' + str(lookup_matrix[i][j][k][0]) + '=' + str(j) + '.' + str(lookup_matrix[i][j][k][1]))
        whereComponentList.append(
            str(tableDictionary[valueElement]) + '.' + str(whereDictionary[valueElement]) + ' between \'' + str(
                args[0]) + '\' and \'' + str(args[1]) + '\'')
        return ' and '.join(whereComponentList)

    # Function to make GroupBy component of the sql query
    def getGroupByComponent(self, partitionElements, valueElement):
        groupbyComponentList = ['1']
    #    print '!!!!!!!!!!!!!!!!!!!!!!'
    #    print partitionElements
    #    print '!!!!!!!!!!!!!!!!!!!!!!'
    #    print valueElement
    #    print 'value element in:' + str(valueElement)
        for items in partitionElements:
            if partitionElements[items] != False:
                groupbyComponentList.append(tableDictionary[items] + '.' + groupbyDictionary[items])
        if groupbyDictionary[valueElement] != False:
            groupbyComponentList.append(tableDictionary[valueElement] + '.' + str(groupbyDictionary[valueElement]))
        return ' , '.join(groupbyComponentList)

    # Function to get the static query from static_queries.py file for numAdoption and attendance
    def getStaticQuery(self, partitionElements, valueElement, dateArgs):
        print "inside static query function"
        temp_list = []
        print "-------------------------"+str(partitionElements)
        print "========================="+str(valueElement)
        if valueElement == 'numAdoption':
            for item in partitionElements:
                if item in categoryDictionary['numAdoptionClub']:
                    temp_list.append(item)
            query_to_return = self.staticQuery(temp_list, valueElement, dateArgs)
        if valueElement == 'attendance':
            for item in partitionElements:
                if item in categoryDictionary['attendanceClub']:
                    temp_list.append(item)
            query_to_return = self.staticQuery(temp_list, valueElement, dateArgs)
        query = "select * hello"
        return query_to_return

    def staticQuery(self,partitionList, valueCondition, dateArgs):
        print "!!!!!!!!!!!!!!!!!!!!!!1"+str(partitionList)
        print "@@@@@@@@@@@@@@@@@@@@@@@"+str(valueCondition)
        for entry in static_query[valueCondition]:
            if sorted(entry) == sorted(tuple(partitionList)):
                squery =  static_query[valueCondition][tuple(partitionList)].replace('from_date',dateArgs[0])
                squery = squery.replace('to_date',dateArgs[1])
        return squery

    # Function to accept query as a string to execute and make dataframe corresponding to that particular query and return that dataframe
    def runQuery(self, query):
        # Make connection with the database
        mysql_cn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd=dg.settings.DATABASES['default']['PASSWORD'], db=dg.settings.DATABASES['default']['NAME'])
        # Making dataframe
        temp_df = psql.read_sql(query, con=mysql_cn)
        mysql_cn.close()
        return temp_df