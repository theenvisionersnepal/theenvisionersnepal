# Generated by Django 3.1.6 on 2021-02-19 10:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('explanation', '0002_auto_20210219_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explanation',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
