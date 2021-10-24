from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model) :
    User =models.OneToOneField(User, on_delete=models.CASCADE)

class Add_plant(models.Model) :

    plant_name = models.CharField(max_length=20)
    price = models.IntegerField()
    Plant_Types_Choices = (('Vegetable', 'Vegetable'),
                           ('Flowering', 'Flowering')
                           )
    plant_type = models.CharField(
        max_length=20,
        choices=Plant_Types_Choices,
        default='Flowering'
    )
    imagefile = models.ImageField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.plant_name


class order_plant1(models.Model) :
    Customer_Name = models.CharField(max_length=25)
    plant_name = models.ForeignKey(Add_plant,on_delete=models.CASCADE)
    qty = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)