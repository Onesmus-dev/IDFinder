# Generated by Django 5.1 on 2024-08-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id_finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idmodel',
            name='id_no',
            field=models.IntegerField(unique=True),
        ),
    ]
