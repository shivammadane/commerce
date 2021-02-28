from django import forms
from .models import *
from datetime import date,timedelta
class orderform(forms.ModelForm):
    class Meta:
        model = order_product
        fields ='__all__'
        exclude=['usr','date','payment_status','payment_id','amount','order_id']

        widgets={
            "fullname":forms.TextInput(attrs={'placeholder':'Full Name','class':'form-control'}),
            "email": forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}),
            "mob1": forms.TextInput(attrs={'placeholder': 'Monile no 1', 'class': 'form-control'}),
            "mob2": forms.TextInput(attrs={'placeholder': 'Mobile2', 'class': 'form-control'}),
            "house_no": forms.TextInput(attrs={'placeholder': 'House No', 'class': 'form-control'}),
            "area_name": forms.TextInput(attrs={'placeholder': 'Area Name', 'class': 'form-control'}),
            "landmark": forms.TextInput(attrs={'placeholder': 'Landmark', 'class': 'form-control'}),
            "pincode": forms.TextInput(attrs={'placeholder': 'Pincode', 'class': 'form-control'}),
            "state_city": forms.TextInput(attrs={'placeholder': 'state/city', 'class': 'form-control'}),
        }



class addproduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude={'rate'}
        widgets = {
            "Subcat":forms.Select(attrs={"class":"form-control"}),
            "name":forms.TextInput(attrs={"placeholder":"Product Name","class":"form-control"}),
            "price": forms.NumberInput(attrs={"placeholder": "Price", "class": "form-control"}),
            "stock": forms.NumberInput(attrs={"placeholder": "Product Stock", "class": "form-control"}),
            "img1": forms.FileInput(attrs={"class": "form-control"}),
            "img2": forms.FileInput(attrs={"class": "form-control"}),
            "img3": forms.FileInput(attrs={"class": "form-control"}),
            "des": forms.Textarea(attrs={"placeholder": "Description", "class": "form-control"}),
            "size": forms.TextInput(attrs={"placeholder": "Size (if required)", "class": "form-control"}),
        }

class subcat(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields ='__all__'
        widgets={
             "cat": forms.Select(attrs={"class": "form-control"}),
             "name": forms.TextInput(attrs={"placeholder": "Product Name", "class": "form-control"}),
                  }

class addcat(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widget={
            "name": forms.TextInput(attrs={"placeholder": "Product Name", "class": "form-control"}),

        }