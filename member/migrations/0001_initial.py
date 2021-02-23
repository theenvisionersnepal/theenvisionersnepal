# Generated by Django 3.1.6 on 2021-02-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('Skills', models.CharField(max_length=256)),
                ('Email', models.CharField(max_length=256)),
                ('Phone', models.CharField(max_length=256)),
                ('Facebook_link', models.CharField(max_length=2048)),
                ('Instagram_link', models.CharField(max_length=2048)),
                ('Co_founder', models.BooleanField(default=False)),
            ],
        ),
    ]
