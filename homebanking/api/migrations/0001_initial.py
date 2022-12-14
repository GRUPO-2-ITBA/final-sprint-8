# Generated by Django 3.2.5 on 2022-08-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_surname', models.CharField(max_length=50)),
                ('employee_hire_date', models.DateField()),
                ('employee_dni', models.TextField()),
                ('branch_id', models.IntegerField()),
                ('employee_address_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'empleado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('movimiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('create_at', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movimientos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.IntegerField()),
                ('branch_name', models.CharField(max_length=50)),
                ('branch_address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sucursal',
                'managed': True,
            },
        ),
    ]
