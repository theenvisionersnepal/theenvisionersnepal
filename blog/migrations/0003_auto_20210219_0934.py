# Generated by Django 3.1.6 on 2021-02-19 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210219_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image_url',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post',
            field=models.TextField(),
        ),
    ]
