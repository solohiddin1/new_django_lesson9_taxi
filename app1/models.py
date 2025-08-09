from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # You can add additional fields if needed

    def __str__(self):
        return self.user.username
    
    
class Client(models.Model):
    name = models.CharField(max_length=60)
    number = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Driver(models.Model):
    name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    vehicle_model = models.CharField(max_length=60)
    license_plate = models.CharField()
    sum_km = models.IntegerField()

    def __str__(self):
        return self.name
    

class Tarif(models.Model):
    title = models.CharField(max_length=50)
    karra = models.IntegerField(choices=[(1,'Econom'),(2,'Comfort'),(3,'Biznes')])

    def __str__(self):
        return self.title
    

class Deal(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    from_where = models.CharField(max_length=60)
    to_where = models.CharField(max_length=60)
    tarif = models.ForeignKey(Tarif,on_delete=models.CASCADE)
    distance = models.IntegerField()
    total_cost = models.DecimalField(max_digits=12,decimal_places=2)
    rate = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])

    def __str__(self):
        return f'Deal {self.id} - {self.client.name} to {self.to_where}'


class Roles(models.Model):
    choices = [
        ('client','client'),
        ('driver','driver'),
        ('admin','admin'),
    ]

    role = models.CharField(max_length=20,choices=choices,unique=True)

    def __str__(self):
        return self.role
    

class Comment(models.Model):
    deal = models.ForeignKey(Deal, related_name='comments', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.client.name} on Deal {self.deal.id}'


"""
TZ

client:

fields:
name   | number  
string | string 


Driver:

fields:
name   | number | avtomobil | sum (/km)  |
string | string | string    | decimal    |  


Deal:

fields:
client      | driver      |qayerdan | qayerga | tarif       | masofa  |             summa            | rate        | comment   |
foreign_key | foreign_key |string   | string  | foreign_key | km(int) | masofa * Driver.sum * tarif  |choice field | charfield |


Tarif:

fields:
title  | narxi *             |
string | int (1 dan 3 gacha) |

ekonom  * 1
premium * 2
biznes  * 3

"""