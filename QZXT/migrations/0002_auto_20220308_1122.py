# Generated by Django 3.2.5 on 2022-03-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QZXT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_0',
            name='ahtc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='dh',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='fjxx',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='gzjl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='hjjl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='jyjl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='mz',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='nl',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='qwxz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='xb',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='xl',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='xm',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='xx',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='zwjs',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_0',
            name='zy',
            field=models.CharField(max_length=32, null=True),
        ),
    ]