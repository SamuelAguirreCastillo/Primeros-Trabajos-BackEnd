# Generated by Django 4.1 on 2022-11-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MultaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multa',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
