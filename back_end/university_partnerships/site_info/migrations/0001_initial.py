# Generated by Django 5.0 on 2023-12-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_api_key', models.CharField(max_length=1000)),
                ('site_name', models.CharField(default='University_Partnerships', max_length=250)),
            ],
            options={
                'verbose_name': 'site_info',
            },
        ),
    ]