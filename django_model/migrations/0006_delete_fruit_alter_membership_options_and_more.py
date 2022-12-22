# Generated by Django 4.1.4 on 2022-12-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_model', '0005_alter_membership_date_joined'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fruit',
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'get_latest_by': ['name', '-date_joined']},
        ),
        migrations.AddField(
            model_name='membership',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterModelTable(
            name='membership',
            table='membership',
        ),
    ]