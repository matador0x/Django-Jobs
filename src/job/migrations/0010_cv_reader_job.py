# Generated by Django 3.1.4 on 2020-12-27 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_cv_reader'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv_reader',
            name='job',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='applay_job', to='job.job'),
            preserve_default=False,
        ),
    ]
