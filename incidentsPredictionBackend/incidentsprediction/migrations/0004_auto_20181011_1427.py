# Generated by Django 2.1.2 on 2018-10-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentsprediction', '0003_auto_20181011_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='value',
            name='parameter',
        ),
        migrations.AddField(
            model_name='parameter',
            name='values',
            field=models.ManyToManyField(to='incidentsprediction.Value'),
        ),
    ]