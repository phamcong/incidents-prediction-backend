# Generated by Django 2.1.2 on 2018-10-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentsprediction', '0005_auto_20181011_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictmodel',
            name='label',
            field=models.CharField(default='', max_length=100),
        ),
    ]