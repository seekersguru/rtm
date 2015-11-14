from django.template.response import TemplateResponse
from django.http import HttpResponse
from models import Places,Iternary
def index(request,params=None,id=None):
    
    #return HttpResponse("rs")       
    return TemplateResponse(request, 'index.html', {"places":Places.objects.all()})

def review_and_verified(request,params=None,id=None):
    #return HttpResponse("rs")       
    return TemplateResponse(request, 'review_and_verified.html', {"nav":"review_and_verified"})

def customer_support(request,params=None,id=None):
    #return HttpResponse("rs")       
    return TemplateResponse(request, 'customer_support.html', {"nav":"customer_support"})

def listing_tour(request,tour_id=None):
    context={}
    if not tour_id:
        context["nav"]="listing_tour"
        context["head"]="Top Packages"
    else:
        place=Places.objects.get(url_property=request.get_full_path())
        
        iternaries=Iternary.objects.filter(place=place)
        context["place"]=place
        context["iternaries"]=iternaries
    
    return TemplateResponse(request, 'listing_tour.html', context)
    
def vip_access(request):
    return TemplateResponse(request, 'vip_access.html', {"nav":"vip_access"})
    
    
def low_price_guaranteed(request):
    return TemplateResponse(request, 'low_price_guaranteed.html', {"nav":"low_price_guaranteed"})

def iternary_detail(request,iternary_id):
    iternary=Iternary.objects.get(url_property=request.get_full_path())
    
    return TemplateResponse(request, 'details.html', {"iternary":iternary})


