from django.db import models

# Create your models here.
from datetime import date
from django.db import models

from tinymce.models import HTMLField
from django.core.exceptions import ObjectDoesNotExist
from django import forms

##aOne place can be nultile itinerary


############# Places starts ##############

## TODO 
    ## add field show /hide.
    ## order 
    #urls etc fine on frontend as well backend + seo implementation
class Places(models.Model):
    #http://royaltripmaker.com/ Select Goa
    name = models.CharField(max_length=128, unique=True)
    
    introduction=HTMLField()
    activity=HTMLField()
    main_image = models.ImageField(upload_to='static/placehome/%Y/%m/%d/%H/%M/%S/',default="None")
    #https://www.google.co.in/?gfe_rd=cr&ei=TcNGVobDMqbv8we_moHIAw&gws_rd=ssl#q=meta+title+length
    meta_title = models.CharField(max_length=60, unique=True)
    #https://www.google.co.in/?gfe_rd=cr&ei=TcNGVobDMqbv8we_moHIAw&gws_rd=ssl#q=meta%20description%20length
    meta_description = models.CharField(max_length=160, unique=True)
    #http://webmasters.stackexchange.com/questions/17740/whats-the-maximum-length-of-the-meta-keywords-tag
    #no official length requirement but generally you'll see people mention anywhere from 100 to 255 characters. 
    meta_keywords = models.CharField(max_length=256, unique=True)
    
    show = models.CharField(max_length=1,default=1)
    url_property = models.CharField(max_length=512,default=1)
    order = models.IntegerField(unique=True,null=True,blank=True)
    
    ## tour/name (unique)  space - > small
#     @property
#     def url_property(self):
#         return "/tour/"+self.name.lower().replace(" ","-")+"/"
    def save(self, force_insert=False, force_update=False):
        self.url_property = "/tour/"+self.name.lower().replace(" ","-")+"/"
        super(Places, self).save(force_insert, force_update)
    
    def __str__(self):
        return self.name
       
## TODO LATER | Gallery 
class PlaceImages(models.Model):
    image = models.ImageField(upload_to='static/placeimages/%Y/%m/%d/%H/%M/%S/')
    place = models.ForeignKey(Places)
    def __str__(self):
        return self.place.name
    ### http://royaltripmaker.com/trip.aspx 
    ## name / description /> show 
    
############# Places ends ##############



############ Itinerary starts #############
# TODO 
# urls etc fine on frontend as well backend + seo implementation
# Also add this to new something like places. Group
class Iternary(models.Model):
    #http://royaltripmaker.com/ Select Goa
    name = models.CharField(max_length=128, unique=True)
    introduction=HTMLField()
    location = models.CharField(max_length=128)
    duration = models.CharField(max_length=256)
    price = models.IntegerField()
    overview=HTMLField()
    pricing_and_schedule=HTMLField()
    iternary=HTMLField()
    iternary=HTMLField() ## co
    latitude=models.FloatField()
    longitude=models.FloatField()
    #https://www.google.co.in/?gfe_rd=cr&ei=TcNGVobDMqbv8we_moHIAw&gws_rd=ssl#q=meta+title+length
    meta_title = models.CharField(max_length=60, unique=True)
    #https://www.google.co.in/?gfe_rd=cr&ei=TcNGVobDMqbv8we_moHIAw&gws_rd=ssl#q=meta%20description%20length
    meta_description = models.CharField(max_length=160, unique=True)
    #http://webmasters.stackexchange.com/questions/17740/whats-the-maximum-length-of-the-meta-keywords-tag
    #no official length requirement but generally you'll see people mention anywhere from 100 to 255 characters. 
    meta_keywords = models.CharField(max_length=256, unique=True)
    place=models.ForeignKey(Places)
    ## page url  space - > small
    ## package/name (unique) 
    ## Case sensitive
    url_property = models.CharField(max_length=512,default=1)
    
    main_image = models.ImageField(upload_to='static/iternaryimage/%Y/%m/%d/%H/%M/%S/')
    
    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Iternary.objects.get(name__iexact=name)
        except ObjectDoesNotExist:
            return name
        raise forms.ValidationError('Iternary already exists.')    
    
#     @property
#     def url_property(self):
#         return self.name.lower().replace(" ","-")
    def save(self, force_insert=False, force_update=False):
        self.url_property = "/package/"+self.name.lower().replace(" ","-")+"/"
        super(Iternary, self).save(force_insert, force_update)
    
    def __str__(self):
        return self.name
            
class IternaryImages(models.Model):
    image = models.ImageField(upload_to='static/placeimages/%Y/%m/%d/%H/%M/%S/')
    iternary = models.ForeignKey(Iternary)

class Enquiry(models.Model):
    name = models.CharField(max_length=128)
    email=models.EmailField(max_length=512)
    mobile=models.IntegerField()
    date=models.DateField()
    comment=models.TextField()
#Separate 
class InfoIternary(models.Model):
    contact_person = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=512)
    website=models.CharField(max_length=128)
############ ITernary ends #############


class Themes(models.Model):
    #http://royaltripmaker.com/ Select Goa
    name = models.CharField(max_length=128, unique=True)
    introduction=HTMLField()
    main_image = models.ImageField(upload_to='static/themes/%Y/%m/%d/%H/%M/%S/',default="None")
    iternaries=models.ManyToManyField(Iternary)
    url_property = models.CharField(max_length=512,default=1)
    order = models.IntegerField(unique=True,null=True,blank=True)
    meta_title = models.CharField(max_length=60,default='')
    meta_description = models.CharField(max_length=160,default='') 
    meta_keywords = models.CharField(max_length=256,default='')
    #intro=HTMLField()
    def __str__(self):
        return self.name    
    def save(self, force_insert=False, force_update=False):
        self.url_property = "/theme/"+self.name.lower().replace(" ","-")+"/"
        super(Themes, self).save(force_insert, force_update)
    #Many to Many fir itinerary
# Show same like [places ]
class SliderImages(models.Model):
    image = models.ImageField(upload_to='static/slider/') 



  
class ReviewVerified(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    trip_name = models.CharField(max_length=128)
    rating = models.CharField(max_length=128)
    comment=models.TextField()
class GalleryImages(models.Model):
    image = models.ImageField(upload_to='static/galary/')
    place=models.ForeignKey(Iternary)
    def __str__(self):
        return self.place.name

class IternaryEnquiry(models.Model):
    name = models.CharField(max_length=128)
    email=models.EmailField(max_length=512)
    iternaryenquiry=models.EmailField(max_length=512,null=True,blank=True)
    mobile=models.IntegerField()
    date=models.DateField()
    comment=models.TextField()

class VipAccess(models.Model):
    name = models.CharField(max_length=128)
    email=models.EmailField(max_length=512)
    mobile=models.IntegerField()
    date=models.DateField()
    comment=models.TextField()

class BestSelling(models.Model):
    name = models.CharField(max_length=128)
    order = models.IntegerField(null=True,blank=True,unique=True)
    best = models.ForeignKey(Iternary)





class PlanMyTrip(models.Model):
    name = models.CharField(max_length=128)
    email=models.EmailField(max_length=512)
    to = models.CharField(max_length=128)
    fr = models.CharField(max_length=128)
    date=models.DateField()
    mode_of_transport = models.CharField(max_length=128)
    no_of_passenger = models.CharField(max_length=128)
    discount_criteria = models.CharField(max_length=128)
    mobile=models.IntegerField()
 



      

