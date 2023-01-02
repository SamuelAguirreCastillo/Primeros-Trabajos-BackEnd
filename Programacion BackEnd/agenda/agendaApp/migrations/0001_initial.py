# Generated by Django 4.1 on 2022-11-28 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaCita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('celular', models.PositiveIntegerField()),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=10)),
                ('motivo', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='PreguntaFrecuente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]
