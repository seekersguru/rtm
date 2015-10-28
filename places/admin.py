from django.contrib import admin
# Register your models here.

from .models import Places,PlaceImages ,Iternary,IternaryImages,IternaryEnquiry,InfoIternary
from django.contrib.auth.models import User, Group

class PlacesAdmin(admin.ModelAdmin):
    model=Places
    list_display = ['name',]
  
# Register your models here.
admin.site.register(Places,PlacesAdmin)
admin.site.register(PlaceImages)
admin.site.register(Iternary)
admin.site.register(IternaryImages)
admin.site.register(IternaryEnquiry)
admin.site.register(InfoIternary)

admin.site.unregister(User)
admin.site.unregister(Group)
