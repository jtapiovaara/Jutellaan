# Generated by Django 3.1.2 on 2020-10-13 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tulkkaa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kielikoodi', models.CharField(max_length=2)),
                ('kielinimi', models.CharField(max_length=25)),
                ('fkieli', models.BooleanField(default=True)),
                ('tkieli', models.BooleanField(default=True)),
                ('lippu', models.FileField(upload_to='')),
            ],
        ),
    ]
