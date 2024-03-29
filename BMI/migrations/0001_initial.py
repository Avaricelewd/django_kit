# Generated by Django 2.2.3 on 2019-07-27 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BMI',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='编号')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='日期')),
                ('height', models.DecimalField(decimal_places=3, max_digits=3, verbose_name='身高')),
                ('weight', models.DecimalField(decimal_places=3, max_digits=3, verbose_name='体重')),
                ('state', models.CharField(max_length=8, verbose_name='状态')),
                ('BMI', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='BMI指数')),
            ],
        ),
    ]
