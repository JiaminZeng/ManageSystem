# Generated by Django 3.2.5 on 2022-03-22 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QZXT', '0009_job_zt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='djsj',
            field=models.CharField(default='-', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='sj',
            field=models.CharField(default='-', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='zcsj',
            field=models.CharField(default='-', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_1',
            name='zcsj',
            field=models.CharField(default='-', max_length=50, null=True),
        ),
    ]