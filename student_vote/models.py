from django.db import models

# Create your models here.

class option(models.Model):
    GENDER_CHOICES = (
        (0,'未选择、弃票'),
        (1,'支持'),
        (2,'不支持'),
    )
    name = models.CharField(verbose_name='姓名',max_length=20)
    support = models.IntegerField(verbose_name='支持',choices=GENDER_CHOICES,default=0,null=True,blank=True)
    onsupport = models.IntegerField(verbose_name='不支持',choices=GENDER_CHOICES,default=0,null=True,blank=True)
    waiver = models.IntegerField(verbose_name='弃票',choices=GENDER_CHOICES,default=0,null=True,blank=True)
