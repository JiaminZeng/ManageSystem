# Generated by Django 3.2.5 on 2022-03-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QZXT', '0008_job_fbzyhm'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='zt',
            field=models.IntegerField(default=1),
        ),
    ]
