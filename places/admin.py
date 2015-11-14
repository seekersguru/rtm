from django.contrib import admin
# Register your models here.

from .models import Places,PlaceImages ,Iternary,IternaryImages,IternaryEnquiry,InfoIternary
from django.contrib.auth.models import User, Group

class PlacesAdmin(admin.ModelAdmin):
    model=Places
    list_display = ['name','url_property']
class IternaryAdmin(admin.ModelAdmin):
    model=Iternary
    list_display = ['name','url_property',] 
  
  
# Register your models here.
admin.site.register(Places,PlacesAdmin)
admin.site.register(PlaceImages)
admin.site.register(Iternary,IternaryAdmin)
admin.site.register(IternaryImages)
admin.site.register(IternaryEnquiry)
admin.site.register(InfoIternary)

admin.site.unregister(User)
admin.site.unregister(Group)
