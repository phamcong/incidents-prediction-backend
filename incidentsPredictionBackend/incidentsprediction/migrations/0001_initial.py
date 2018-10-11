# Generated by Django 2.1.2 on 2018-10-11 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('label', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PredictModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidentsprediction.Parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_value', models.CharField(choices=[('NUMBER', 'Number'), ('STRING', 'String')], default='STRING', max_length=10)),
                ('value', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='parameter',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidentsprediction.Value'),
        ),
    ]
