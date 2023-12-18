# Generated by Django 5.0 on 2023-12-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_info', '0002_alter_site_info_google_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_info',
            name='site_url',
            field=models.CharField(default='127.0.0.1:8000', max_length=250),
        ),
        migrations.AlterField(
            model_name='site_info',
            name='google_api_key',
            field=models.CharField(max_length=1000),
        ),
    ]
