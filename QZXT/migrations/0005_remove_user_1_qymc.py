# Generated by Django 3.2.5 on 2022-03-18 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QZXT', '0004_company_user_1_user_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_1',
            name='qymc',
        ),
    ]
