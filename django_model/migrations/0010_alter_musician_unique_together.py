# Generated by Django 4.1.4 on 2022-12-22 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_model', '0009_fruit'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='musician',
            unique_together={('first_name', 'last_name')},
        ),
    ]
