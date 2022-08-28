from django import forms
import datetime

lista = [('PERSONAL', 'PERSONAL'),  ('PRENDARIO', 'PRENDARIO'),
         ('HIPOTECARIO', 'HIPOTECARIO'), ('CONSUMO', 'CONSUMO'), ('OTROS', 'OTROS')]


class PrestamoForm(forms.Form):
    loan_date = forms.DateField(
        label='Fecha de prestamo', initial=datetime.date.today)
    loan_total = forms.IntegerField(label='Monto del prestamo', required=True)
    loan_payment = forms.CharField(
        label='Tipo de prestamo', widget=forms.Select(choices=lista))
