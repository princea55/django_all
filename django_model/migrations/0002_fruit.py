# Generated by Django 4.1.4 on 2022-12-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]