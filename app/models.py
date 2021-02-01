from django.db import models

class Costumer(models.Model):
    Cname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class Product(models.Model):
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    price = models.PositiveIntegerField(default=0)
    PR_id = models.PositiveIntegerField(default=0)
    PR_number = models.PositiveIntegerField(default=0)
    Total = 0
    

class Payment(models.Model):
    PA_type = models.CharField(max_length=32 , default= 0)
    amount = models.PositiveIntegerField(default=0)
    buyer = models.CharField(max_length=32 )
     

class User():
    name = models.CharField(max_length=32)
    Email = models.EmailField(max_length=50)
    psw = models.CharField(max_length=32)
    pswrepeat = models.CharField(max_length=32)

    # def check():
    #     return psw == pswrepeat 
            
        



    