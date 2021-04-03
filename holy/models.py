from django.db import models
from django.contrib.auth.models import User

class CATE_GORY(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class NEW_ARRIVAL(models.Model):
    image=models.FileField(null=True)
    category=models.ForeignKey(CATE_GORY,on_delete=models.CASCADE,default=1)
    name=models.CharField(null=True,max_length=20)
    price=models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(NEW_ARRIVAL,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.price

class Customer_detail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first=models.CharField(max_length=20)
    last=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=40)
    country=models.CharField(max_length=10)
    add1=models.TextField(max_length=50)
    add2=models.TextField(max_length=50)
    city=models.CharField(max_length=20)
    dist=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=6)
    
class Order_place(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer_detail,on_delete=models.CASCADE)
    item=models.ForeignKey(NEW_ARRIVAL,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return self.user


    @property
    def total_cost(self):
        return self.quantity * self.item.price
