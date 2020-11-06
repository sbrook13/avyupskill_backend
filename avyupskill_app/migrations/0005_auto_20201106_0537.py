# Generated by Django 3.1.2 on 2020-11-06 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avyupskill_app', '0004_auto_20201105_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='aiare_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='cost',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='details_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='course',
            name='provider_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]