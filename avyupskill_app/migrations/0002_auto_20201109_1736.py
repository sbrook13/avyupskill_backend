# Generated by Django 3.1.2 on 2020-11-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avyupskill_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
