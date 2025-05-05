from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nom", required=True, widget=forms.TextInput(attrs={'class':'form-control'}), min_length=3, max_length=100)
    correo = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class':'form-control'}), min_length=3, max_length=100)
    mensaje = forms.CharField(label="Message", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Votre message'}), min_length=10, max_length=1000)