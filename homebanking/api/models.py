from django.db import models


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.IntegerField()
    branch_name = models.CharField(max_length=50)
    branch_address = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'sucursal'


class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True)
    account_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    # This field type is a guess.
    create_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'movimientos'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50)
    employee_surname = models.CharField(max_length=50)
    employee_hire_date = models.TextField()
    # Field name made lowercase.
    employee_dni = models.TextField()
    branch_id = models.IntegerField()
    employee_address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'empleado'
