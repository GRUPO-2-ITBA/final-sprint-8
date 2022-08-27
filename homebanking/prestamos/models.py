from django.db import models
import uuid

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_payment = models.CharField(max_length=50)
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'prestamo'
        