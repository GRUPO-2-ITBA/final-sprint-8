from django import forms
import datetime

lista = [('1', 'PERSONAL'),  ('2', 'PRENDARIO'),
         ('3', 'HIPOTECARIO'), ('4', 'CONSUMO'), ('5', 'OTROS')]


class PrestamoForm(forms.Form):
    customer_id = forms.CharField(label="cliente_id", required=True)
    loan_date = forms.DateField(
        label='Fecha de prestamo', initial=datetime.date.today)
    loan_total = forms.IntegerField(label='Monto del prestamo', required=True)
    loan_payment = forms.CharField(
        label='Tipo de prestamo', widget=forms.Select(choices=lista))
