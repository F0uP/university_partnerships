# Generated by Django 5.0 on 2023-12-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_alter_university_partner_universities'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'Universitie'},
        ),
        migrations.AddField(
            model_name='university',
            name='lat',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='university',
            name='lng',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]