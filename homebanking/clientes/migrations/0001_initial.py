# Generated by Django 3.2.5 on 2022-08-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.DateField()),
                ('branch_id', models.IntegerField()),
                ('customer_type_id', models.IntegerField(blank=True, null=True)),
                ('address_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
    ]