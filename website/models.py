from django.contrib.auth.models import User
from django.db import models


# Business Model
class Business(models.Model):
    '''
    This Model defines all of the relationships and attributes of the Business table.

        Author: Group

        Methods:
            __str__ -- user
    '''
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length= 50)

    def __str__(self):
        ''' returns a string representation of the model '''
        return self.name

# Product Model
class Product(models.Model):
    '''
    This Model defines all the relationships and attributes of the Products table in the
        database.

        Author: Group

        Methods:
        __str__ -- title
    '''
    business = models.ForeignKey(Business, on_delete= models.PROTECT)
    status = models.ForeignKey(Status, on_delete= models.PROTECT)
    UPC = models.CharField(max_length=12)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        ''' returns a string representation of the model '''
        return self.title


class Status(models.Model):
    '''
    This Model defines the attributes of the Status table in the database.
    '''
    name = models.CharField(max_length= 50)

    def __str__(self):
        ''' returns a string representation of the model '''
        return self.name