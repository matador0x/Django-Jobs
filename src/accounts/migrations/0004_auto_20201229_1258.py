# Generated by Django 3.1.4 on 2020-12-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201229_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(max_length=15, null=True),
        ),
    ]