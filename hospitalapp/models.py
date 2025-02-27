from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=100)
    #charfields is for text
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class staff(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return self.firstname, self.lastname

class ward(models.Model):
    name = models.CharField(max_length=100)
    totalbeds = models.IntegerField()
    availablebeds = models.IntegerField()


    def __str__(self):
        return self.name
