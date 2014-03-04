from django.db import models

from dashboard.models import CocoModel

class Partner(CocoModel):
    id = models.AutoField(primary_key = True)
    old_coco_id = models.BigIntegerField()
    partner_name = models.CharField(max_length=100)
    date_of_association = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=500, blank=True)
    
    def __unicode__(self):
        return self.partner_name
