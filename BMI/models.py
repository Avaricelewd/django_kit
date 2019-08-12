from django.db import models


# Create your models here.
class BMI(models.Model):
    no = models.AutoField(verbose_name='编号', unique=True,primary_key=True)
    date = models.DateTimeField(verbose_name='日期', auto_now_add=True)
    height = models.DecimalField(verbose_name='身高', max_digits=3, decimal_places=3)
    weight = models.DecimalField(verbose_name='体重', max_digits=3, decimal_places=3)
    state = models.CharField(verbose_name='状态', max_length=8)
    BMI = models.DecimalField(verbose_name='BMI指数', max_digits=2, decimal_places=1)
