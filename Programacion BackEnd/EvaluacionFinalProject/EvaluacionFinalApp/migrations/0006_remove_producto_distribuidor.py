# Generated by Django 4.1 on 2022-12-26 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EvaluacionFinalApp', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='distribuidor',
        ),
    ]
