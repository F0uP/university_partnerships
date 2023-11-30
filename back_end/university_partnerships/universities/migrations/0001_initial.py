# Generated by Django 3.2.21 on 2023-11-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=200)),
                ('partner_universities', models.ManyToManyField(blank=True, related_name='_universities_university_partner_universities_+', to='universities.University')),
            ],
        ),
    ]
