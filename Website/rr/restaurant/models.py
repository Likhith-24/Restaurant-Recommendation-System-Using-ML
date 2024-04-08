from django.db import models
from django.utils import *
# Create your models here.
class Restaurant(models.Model):
    """
    Django Restaurent Model
    """
    rest_id= models.IntegerField(default=0)
    Name = models.CharField(max_length=200,null=True)
    Online_Orders = models.BooleanField(default=False, null=True)
    Booking_Table = models.BooleanField(default=False, null=True)
    Ratings = models.FloatField(default=0)
    Votes = models.IntegerField(default=0)
    Restaurant_Type = models.CharField(max_length=200,null=True)
    Cuisines = models.CharField(max_length=200,null=True)
    Cost= models.IntegerField(default=0)
    Type =  models.CharField(max_length=200,null=True)
    City= models.CharField(max_length=200,null=True)
    Mean_Rating= models.FloatField(default=0)
    User_Ratings = models.FloatField(default=0)


    def __str__(self):
        return self.Name


class Order(models.Model):
    # Define the fields for the new table
    order_id= models.IntegerField(default=0 )
    
class OrderPlaced(models.Model):
    user= models.CharField(max_length=200,null=True)
    order_id= models.IntegerField(default=0 )
    order_date = models.DateField()
    Ratings = models.FloatField(default=0)
    Name = models.CharField(max_length=200,null=True)
    City= models.CharField(max_length=200,null=True)
    Cost= models.IntegerField(default=0)
    class Meta:
        verbose_name = ("Orderplaced")
        verbose_name_plural = ("Orderplaceds")

    def __str__(self):
        return self.name


    