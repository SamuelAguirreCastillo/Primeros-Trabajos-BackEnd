# Generated by Django 4.1 on 2022-12-26 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EvaluacionFinalApp', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='distribuidor',
        ),
        migrations.RemoveField(
            model_name='devolucion',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='devolucion',
            name='distribuidor',
        ),
        migrations.RemoveField(
            model_name='devolucion',
            name='vendedor',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='distribuidor',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.RemoveField(
            model_name='vendedor',
            name='distribuidor',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Devolucion',
        ),
        migrations.DeleteModel(
            name='Distribuidor',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]
