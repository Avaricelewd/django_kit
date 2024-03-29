# Generated by Django 2.2.3 on 2019-08-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_vote', '0003_auto_20190801_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='option_1',
        ),
        migrations.AddField(
            model_name='option',
            name='onsupport',
            field=models.IntegerField(choices=[(0, '未选择、弃票'), (1, '支持'), (2, '不支持')], default=0, verbose_name='不支持'),
        ),
        migrations.AddField(
            model_name='option',
            name='support',
            field=models.IntegerField(choices=[(0, '未选择、弃票'), (1, '支持'), (2, '不支持')], default=0, verbose_name='支持'),
        ),
        migrations.AddField(
            model_name='option',
            name='waiver',
            field=models.IntegerField(choices=[(0, '未选择、弃票'), (1, '支持'), (2, '不支持')], default=0, verbose_name='弃票'),
        ),
    ]
