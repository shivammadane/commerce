from django.db import models
from django.contrib.auth.models import User
# Create your models here.
status=[['Order Confirmed','Order Confirmed'],
        ['Shipped','Shipped'],
        ['Out for Delivery','Out for Delivery'],
        ['Delivered','Delivered']]


class Category(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class Subcategory(models.Model):
    cat=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.cat.name +"--"+self.name

class Product(models.Model):
    Subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100,null=True)
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    img1 =models.FileField(null=True)
    img2 = models.FileField(null=True)
    img3 = models.FileField(null=True)
    des=models.TextField(null=True)
    size=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.Subcat.name +"--"+self.name




class  userdetail(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mob=models.IntegerField(null=True)
    address=models.TextField(null=True)
    img=models.FileField(null=True)

class AddToCart(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pro=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    totalprice=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    size=models.CharField(max_length=100,null=True,blank=True)

class order_product(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fullname=models.CharField(max_length=100,null=True)
    house_no=models.CharField(max_length=100,null=True,blank=True)
    area_name = models.CharField(max_length=100, null=True)
    landmark = models.CharField(max_length=100, null=True,blank=True)
    state_city = models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    pincode= models.CharField(max_length=100, null=True)
    mob1 = models.CharField(max_length=100, null=True)
    mob2 = models.CharField(max_length=100, null=True,blank=True)
    date=models.DateField(blank=True,null=True)
    order_id = models.CharField(max_length=100, null=True,blank=True)
    payment_status=models.CharField(max_length=100,default='Not Done',blank=True)
    payment_id=models.CharField(max_length=100, null=True,blank=True)
    amount=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.fullname +"--"+self.order_id
class order_product_detail(models.Model):
    order_detail=models.ForeignKey(order_product, on_delete=models.CASCADE, null=True)
    pro = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,blank=True)
    quantity=models.IntegerField(null=True)
    estimated_date=models.DateField(null=True,blank=True)
    total_amount=models.IntegerField(null=True)
    status = models.CharField(max_length=100, null=True, choices=status,blank=True)


class new(models.Model):
    u=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    p=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    m=models.TextField(null=True)
    d=models.DateField(null=True,blank=True)
