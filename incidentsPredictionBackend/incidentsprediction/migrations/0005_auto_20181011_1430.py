# Generated by Django 2.1.2 on 2018-10-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentsprediction', '0004_auto_20181011_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictmodel',
            name='parameter',
        ),
        migrations.AddField(
            model_name='predictmodel',
            name='parameters',
            field=models.ManyToManyField(to='incidentsprediction.Parameter'),
        ),
    ]
