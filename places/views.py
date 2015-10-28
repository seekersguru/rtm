from django.template.response import TemplateResponse
from django.http import HttpResponse
from models import Places
def index(request,params=None,id=None):
    from models import Places
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
        place=Places.objects.get(pk=int(tour_id))
        context["head"]=place.name
    return TemplateResponse(request, 'listing_tour.html', context)
    
def vip_access(request):
    return TemplateResponse(request, 'vip_access.html', {"nav":"vip_access"})
    
    
def low_price_guaranteed(request):
    return TemplateResponse(request, 'low_price_guaranteed.html', {"nav":"low_price_guaranteed"})

def iternary_detail(request):
    return TemplateResponse(request, 'details.html', {"nav":"low_price_guaranteed"})