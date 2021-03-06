# Generated by Django 3.0.4 on 2020-04-06 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='img',
            field=models.ImageField(default=' ', upload_to='notes-img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
