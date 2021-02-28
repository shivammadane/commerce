from django import forms
from .models import *
from datetime import date,timedelta
class addproduct(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'
        exclude=['Subcat']
        widget={
        "name":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
        "price":forms.NumberInput(attrs={'placeholder':'price','class':'form-control'}),
        "stock": forms.NumberInput(attrs={'placeholder': 'Stock', 'class': 'form-control'}),
        "img1":forms.FileInput(attrs={'placeholder':'Img1'}),
        "img2": forms.FileInput(attrs={'placeholder': 'Img2'}),
        "img3": forms.FileInput(attrs={'placeholder': 'Img3'}),
        "des": forms.TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}),
        "rate": forms.NumberInput(attrs={'placeholder': 'Rating', 'class': 'form-control'}),
            }