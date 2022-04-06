from django.db import models

from django.db import models

class Area_info(models.Model):
    area = models.CharField(max_length=200)

    class Meta:
        db_table = 'area_info'

    def __str__(self):
        return super().__str__()

class Branch_office(models.Model):
    branch_name = models.CharField(max_length=200)

    area = models.ForeignKey('Area_info', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'branch_office'

    def _str__(self):
        return super().__str__()