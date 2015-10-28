"""rtm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from tinymce import urls as tiny_urls
from places.views import index,review_and_verified,customer_support \
    ,listing_tour,vip_access,low_price_guaranteed,iternary_detail
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include(tiny_urls)),
    url(r'^$', index, name='index_method'),
    url(r'^reviewed-and-verified/$', review_and_verified, name='reviewed-and-verified'),
    url(r'^customer-support/$', customer_support, name='customer-support'),
    
    ## This one is for top packages 
    url(r'^listing-tour/$', listing_tour, name='listing-tour'),
    url(r'^listing-tour/(?P<tour_id>\d+)/$', listing_tour, name='listing-tour_by_id'),
    
    url(r'^vip-access/$', vip_access, name='vip-access'),
    url(r'^low-price-guaranteed/$', low_price_guaranteed, name='low_price_guaranteed'),
    url(r'^detail/$', iternary_detail, name='iternary_detail'),
    
    
    
    
    
    
]

admin.site.site_header = 'RTM'
admin.site.site_title = 'RTM'
admin.site.index_title = 'RTM'
