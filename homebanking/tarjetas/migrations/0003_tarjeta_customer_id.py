# Generated by Django 3.2.5 on 2022-08-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarjetas', '0002_alter_tarjeta_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta',
            name='customer_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
