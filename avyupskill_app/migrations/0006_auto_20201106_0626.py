# Generated by Django 3.1.2 on 2020-11-06 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avyupskill_app', '0005_auto_20201106_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='contact_email',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='class_type',
            field=models.CharField(choices=[('1', 'AIARE 1 '), ('2', 'AIARE 2 '), ('3', 'Avalanche Rescue')], max_length=1),
        ),
    ]