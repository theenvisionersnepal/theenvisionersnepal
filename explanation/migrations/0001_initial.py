# Generated by Django 3.1.6 on 2021-02-19 09:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
