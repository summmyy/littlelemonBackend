from django.db import models
from PIL import Image
from datetime import datetime

# Create your models here.
class Menu(models.Model):
    # id = models.IntegerField(primary_key=True,)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField
    description = models.CharField(max_length=500, default="This is a little lemon dish")
    image = models.ImageField(default='./static/img/salad.jpg', upload_to='menu-images/')

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField( default=1)
    BookingDate = models.DateTimeField(default=datetime.now)
    email = models.CharField(max_length=255, default='little@lemon.com')
    phone_number = models.IntegerField( default=0)

    def __str__(self) -> str:
        return f'{self.name} : {self.no_of_guests}'

class Employees(models.Model):
    name = models.CharField(max_length= 200)
    department = models.CharField(max_length= 200)
