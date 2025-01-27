from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['fecha', 'numero', 'subtotal', 'impuestos', 'total']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'numero': forms.TextInput(attrs={'placeholder': 'Número de factura'}),
            'subtotal': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'impuestos': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'total': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }
