# Generated by Django 3.2.21 on 2023-11-30 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=200)),
                ('project_description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=500)),
                ('university_main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_universityMain', to='universities.university')),
                ('university_sec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_universitySec', to='universities.university')),
            ],
        ),
    ]
