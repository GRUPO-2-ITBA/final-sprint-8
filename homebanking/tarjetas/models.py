from django.db import models

# Create your models here.


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.CharField(unique=True, max_length=50)
    card_expiration_date = models.TextField()
    card_issue_date = models.TextField()
    card_cvv = models.CharField(max_length=3)
    card_type = models.TextField()
    customer_id = models.IntegerField()
    card_brand_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_subname = models.TextField()
    dob = models.DateField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    customer_type_id = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
