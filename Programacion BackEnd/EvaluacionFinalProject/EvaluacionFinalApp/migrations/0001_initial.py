# Generated by Django 4.1 on 2022-12-21 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Distribuidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('region', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=80)),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.distribuidor')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('contrasena', models.CharField(max_length=120)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=30)),
                ('valor', models.PositiveIntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.categoria')),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.distribuidor')),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('cantidad', models.PositiveIntegerField()),
                ('monto_clp', models.DecimalField(decimal_places=2, max_digits=8)),
                ('monto_dolar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.cliente')),
                ('detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.detalle')),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.distribuidor')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.vendedor')),
            ],
        ),
        migrations.AddField(
            model_name='detalle',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.producto'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='distribuidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionFinalApp.distribuidor'),
        ),
    ]
