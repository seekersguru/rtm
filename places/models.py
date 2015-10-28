from django.db import models

# Create your models here.

from django.db import models

from tinymce.models import HTMLField

############ ITernary starts #############
# Create your models here.
class Iternary(models.Model):
    #http://royaltripmaker.com/ Select Goa
    name = models.CharField(max_length=128, unique=True)
    location = models.CharField(max_length=128)
    duration = models.IntegerField()
    price = models.IntegerField()
    overview=HTMLField()
    pricing_and_schedule=HTMLField()
    iternary=HTMLField()
    iternary=HTMLField()
    latitude=models.FloatField()
    longitude=models.FloatField()

class IternaryImages(models.Model):
    image = models.ImageField(upload_to='static/placeimages/%Y/%m/%d/%H/%M/%S/')
    iternary = models.ForeignKey(Iternary)

class IternaryEnquiry(models.Model):
    name = models.CharField(max_length=128)
    email=models.EmailField(max_length=512)
    mobile=models.IntegerField()
    date=models.DateField()
    subject=models.TextField()

class InfoIternary(models.Model):
    contact_person = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=512)
    website=models.CharField(max_length=128)
############ ITernary ends #############

############# Places starts ##############
# Create your models here.
class Places(models.Model):
    #http://royaltripmaker.com/ Select Goa
    name = models.CharField(max_length=128, unique=True)
    introduction=HTMLField()
    activity=HTMLField()
    main_image = models.ImageField(upload_to='static/placehome/%Y/%m/%d/%H/%M/%S/',default="None")
    


class PlaceImages(models.Model):
    image = models.ImageField(upload_to='static/placeimages/%Y/%m/%d/%H/%M/%S/')
    place = models.ForeignKey(Places)
    
    
############# Places ends ##############