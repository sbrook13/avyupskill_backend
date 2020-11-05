# Generated by Django 3.1.2 on 2020-11-05 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avyupskill_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 'The Worst'), ('2', 'Meh'), ('3', 'Average'), ('4', 'Yay'), ('5', 'The Best')], max_length=1)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avyupskill_app.area')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL, verbose_name='The Reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=400)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avyupskill_app.area')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='The Reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='BackcountryDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avyupskill_app.area')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backcountry_day', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
