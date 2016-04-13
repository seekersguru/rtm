from django.contrib import admin
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Register your models here.

from .models import Places,PlaceImages ,Iternary,IternaryImages,IternaryEnquiry,InfoIternary,Themes,SliderImages,ReviewVerified
from django.contrib.auth.models import User, Group

class PlacesAdmin(admin.ModelAdmin):
    model=Places
    list_display = ['name','url_property']
    ordering=('name',)

class IternaryAdmin(admin.ModelAdmin):
    model=Iternary
    list_display = ['name','url_property',]
    ordering=('name',) 
  
class ThemesAdmin(admin.ModelAdmin):
    model=Themes
    list_display = ['name','url_property',] 
    ordering=('name',)  

class IternaryEnquiryAdmin(admin.ModelAdmin):
    model=IternaryEnquiry
    list_display = ['name','email']
    ordering=('name',)
    '''actions = ['send_EMAIL']
    def send_EMAIL(self, request, queryset):
        from django.core.mail import send_mail
        for i in queryset:
            if i.email:
                to = [i.email]
                from_email = settings.EMAIL_HOST_USER #info@royaltripmaker.com
                html_content = render_to_string('email.html',{})
                text_content = strip_tags(html_content) 
                msg = EmailMultiAlternatives("subject", text_content, from_email, to)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                message = get_template('email.html')#.render(Context(ctx))
                msg = EmailMessage('ghfdghd', "message", to=to, from_email=from_email)
                msg.content_subtype = 'html'
                msg.send()
                send_mail('Subject here', 'Here is the message.', 'from@example.com',[i.email],   			fail_silently=False)

        self.message_user(request, "Mail sent successfully ") 
    send_EMAIL.short_description = "Send an email to selected users"'''

class ReviewVerifiedAdmin(admin.ModelAdmin):
    model=ReviewVerified
    list_display = ['trip_name','rating',]
  
# Register your models here.
admin.site.register(Places,PlacesAdmin)
admin.site.register(PlaceImages)
admin.site.register(ReviewVerified,ReviewVerifiedAdmin)
admin.site.register(Iternary,IternaryAdmin)
admin.site.register(IternaryImages)
admin.site.register(IternaryEnquiry,IternaryEnquiryAdmin)
admin.site.register(InfoIternary)
admin.site.register(Themes,ThemesAdmin)
admin.site.register(SliderImages)


admin.site.unregister(User)
admin.site.unregister(Group)
