from django.template.response import TemplateResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from models import Places,Iternary,Themes,SliderImages,Enquiry,ReviewVerified,GalleryImages,\
IternaryEnquiry,VipAccess,BestSelling,PlanMyTrip
from django.http import JsonResponse
import re
def index(request,params=None,id=None):

    errors={}
    if request.method=='GET' and 'planmybutton' in request.GET:
        data= request.GET
        #print data
        name = data['name1']
        email=data['email1']
        to =data['to1']
        fr=data['fr1']  
        date=data['date1']      
        mode_of_transport=data['mode_of_tranport1']
        no_of_passenger=data['no_of_passenger1']
        discount_criteria=data['discount_criteria1']
        phone=request.GET['phone1']
        #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
        obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	fr=fr,mode_of_transport=mode_of_transport,
	no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
        obj.save()
        sub="[Plan My Trip] Mail From Royal Trip Maker"
	msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	frm=email
	to_us=[settings.EMAIL_HOST_USER]
	send_mail(sub,msg,frm,to_us,fail_silently=False)
        messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    if request.method == "GET" and 'search' in request.GET:
        print request.GET
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            model_results = Iternary.objects.filter(name__contains = value)
            if len(model_results)==0:
                return TemplateResponse(request, 'listing_tour.html',{"noresult":"No Result Found"})
            else:
                return TemplateResponse(request, 'listing_tour.html',{"searchs":model_results})
  
    iternary=Iternary.objects.all()
    if request.method=='POST' and 'submitbutton' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone =request.POST['phone']
        comment=request.POST['comment']
        if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
            errors['fields']="Please All Fields A Required "  
        match_exists = re.match("[a-zA-Z0-9]", name)
        if(len(name)<=2):
            errors['name']="minimum length is atleast 4 characters"
        elif(match_exists==None):
            errors['name']="Only letters number _ . - are allowed"
        match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
        if(len(email)==0):
            errors['email']="Please enter email address"
        elif(match_exists==None):
            errors['email']="Please provide valid email address"
	match_exists = re.match("\d{10,20}$", phone)
	if len(phone)==0:
            errors['phone']="please enter phone "
	elif(match_exists==None):
            errors['phone']= "Please provide valid Phone no.only nimber are allowed"
        if errors:
            errors=errors
            messages.error(request, 'Please fill all the correctly once again.')
        else:
	    errors={}
            print name,email,phone,comment
            obj=Enquiry(name=name,email=email,mobile=phone,comment=comment,date=datetime.now())
            obj.save()
            sub="Mail From Royal Trip Maker"
	    msg='From : %s  \n Message : %s'%((email+"   "+"Name :"+name+" "+"Mobile:"+phone),comment)
	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')


    #return HttpResponse("rs")     
    return TemplateResponse(request, 'index.html', {"places":Places.objects.all(),
                                                    "themes":Themes.objects.all(),
                                                    "slider":SliderImages.objects.all(),
                                                    "iternary":iternary,
                                                    "bestselling":BestSelling.objects.all(),
                                                    "review":ReviewVerified.objects.filter().order_by('-id')
                                                    })

def all_review(request,params=None,id=None):
    return TemplateResponse(request, 'all_review.html',{"review":ReviewVerified.objects.filter().order_by('-id')})

def review_and_verified(request,params=None,id=None):
    if request.method=='GET' and 'planmybutton' in request.GET:
        data= request.GET
        #print data
        name = data['name1']
        email=data['email1']
        to =data['to1']
        fr=data['fr1']  
        date=data['date1']      
        mode_of_transport=data['mode_of_tranport1']
        no_of_passenger=data['no_of_passenger1']
        discount_criteria=data['discount_criteria1']
        phone=request.GET['phone1']
        #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
        obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	fr=fr,mode_of_transport=mode_of_transport,
	no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
        obj.save()
        sub="[Plan My Trip] Mail From Royal Trip Maker"
	msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	frm=email
	to_us=[settings.EMAIL_HOST_USER]
	send_mail(sub,msg,frm,to_us,fail_silently=False)
        messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    if request.method == "GET" and 'search' in request.GET:
        print request.GET
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            model_results = Iternary.objects.filter(name__contains = value)
            if len(model_results)==0:
                return TemplateResponse(request, 'listing_tour.html',{"noresult":"No Result Found"})
            else:
                return TemplateResponse(request, 'listing_tour.html',{"searchs":model_results})
    errors={}
    
    if request.method == 'POST' and 'rewiewbutton' in request.POST:
        data = request.POST
        rating=data['rating']
	if request.FILES=='':
	    img=''
	else:
	    img=request.FILES['pic']
	
        #hidden=request.POST['reviewhidden']
        name = request.POST['name']
        city = request.POST['city']
        trip =request.POST['trip']
        comment=request.POST['comment']
       
        #print name,city,trip,comment,rating
        if len(name)==0 or len(trip)==0 or len(rating)==0 or len(comment)==0:
            errors['fields']="Please All Fields A Required "  
        match_exists = re.match("[a-zA-Z0-9]", name)
        if(len(name)<=2):
            errors['name']="minimum length is atleast 4 characters"
        elif(match_exists==None):
            errors['name']="Only letters number _ . - are allowed"
        match_exists = re.match("[a-zA-Z0-9]", city)
        if(len(city)==0):
            errors['city']="Please enter email address"
        elif(match_exists==None):
            errors['city']="Please provide valid email address"
	match_exists = re.match("[a-zA-Z0-9]", trip)
	if len(trip)==0:
            errors['trip']="please enter phone "
	elif(match_exists==None):
            errors['trip']= "Please provide trip name"
        if errors:
            errors=errors
            messages.error(request, 'Please fill all the correctly once again.')
        else:
	    errors={}
            obj=ReviewVerified(pics=img,rating=rating,name=name,city=city,trip_name=trip,comment=comment)
            obj.save()
            messages.success(request, 'Thanks for your Reviews.') 
    if request.method=='POST' and 'submitbutton' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone =request.POST['phone']
        comment=request.POST['comment']
        if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
            errors['fields']="Please All Fields A Required "  
        match_exists = re.match("[a-zA-Z0-9]", name)
        if(len(name)<=2):
            errors['name']="minimum length is atleast 4 characters"
        elif(match_exists==None):
            errors['name']="Only letters number _ . - are allowed"
        match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
        if(len(email)==0):
            errors['email']="Please enter email address"
        elif(match_exists==None):
            errors['email']="Please provide valid email address"
	match_exists = re.match("\d{10,20}$", phone)
	if len(phone)==0:
            errors['phone']="please enter phone "
	elif(match_exists==None):
            errors['phone']= "Please provide valid Phone no.only nimber are allowed"
        if errors:
            errors=errors
            messages.error(request, 'Please fill all the correctly once again.')
        else:
	    errors={}
            #print name,email,phone,comment
            obj=Enquiry(name=name,email=email,mobile=phone,comment=comment,date=datetime.now())
            obj.save()
            sub="Mail From Royal Trip Maker"
	    msg='From : %s  \n Message : %s'%((email+"   "+"Name :"+name+" "+"Mobile:"+phone),comment)
	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    #return HttpResponse("rs")       
    return TemplateResponse(request, 'review_and_verified.html', {"nav":"review_and_verified"})

def customer_support(request,params=None,id=None):
    if request.method=='GET' and 'planmybutton' in request.GET:
        data= request.GET
        #print data
        name = data['name1']
        email=data['email1']
        to =data['to1']
        fr=data['fr1']  
        date=data['date1']      
        mode_of_transport=data['mode_of_tranport1']
        no_of_passenger=data['no_of_passenger1']
        discount_criteria=data['discount_criteria1']
        phone=request.GET['phone1']
        #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
        obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	fr=fr,mode_of_transport=mode_of_transport,
	no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
        obj.save()
        sub="[Plan My Trip] Mail From Royal Trip Maker"
	msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	frm=email
	to_us=[settings.EMAIL_HOST_USER]
	send_mail(sub,msg,frm,to_us,fail_silently=False)
        messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    if request.method == "GET" and 'search' in request.GET:
        print request.GET
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            model_results = Iternary.objects.filter(name__contains = value)
            if len(model_results)==0:
                return TemplateResponse(request, 'listing_tour.html',{"noresult":"No Result Found"})
            else:
                return TemplateResponse(request, 'listing_tour.html',{"searchs":model_results})
 
    errors={}
    if request.method=='POST' and 'submitbutton' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone =request.POST['phone']
        comment=request.POST['comment']
        if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
            errors['fields']="Please All Fields A Required "  
        match_exists = re.match("[a-zA-Z0-9]", name)
        if(len(name)<=2):
            errors['name']="minimum length is atleast 4 characters"
        elif(match_exists==None):
            errors['name']="Only letters number _ . - are allowed"
        match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
        if(len(email)==0):
            errors['email']="Please enter email address"
        elif(match_exists==None):
            errors['email']="Please provide valid email address"
	match_exists = re.match("\d{10,20}$", phone)
	if len(phone)==0:
            errors['phone']="please enter phone "
	elif(match_exists==None):
            errors['phone']= "Please provide valid Phone no.only nimber are allowed"
        if errors:
            errors=errors
            messages.error(request, 'Please fill all the correctly once again.')
        else:
	    errors={}
            #print name,email,phone,comment
            obj=Enquiry(name=name,email=email,mobile=phone,comment=comment,date=datetime.now())
            obj.save()
            sub="Mail From Royal Trip Maker"
	    msg='From : %s  \n Message : %s'%((email+"   "+"Name :"+name+" "+"Mobile:"+phone),comment)
	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    #return HttpResponse("rs")       
    return TemplateResponse(request, 'customer_support.html', {"nav":"customer_support"})

def listing_tour(request,tour_id=None):
    if request.method=='GET' and 'planmybutton' in request.GET:
        data= request.GET
        #print data
        name = data['name1']
        email=data['email1']
        to =data['to1']
        fr=data['fr1']  
        date=data['date1']      
        mode_of_transport=data['mode_of_tranport1']
        no_of_passenger=data['no_of_passenger1']
        discount_criteria=data['discount_criteria1']
        phone=request.GET['phone1']
        #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
        obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	fr=fr,mode_of_transport=mode_of_transport,
	no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
        obj.save()
        sub="[Plan My Trip] Mail From Royal Trip Maker"
	msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	frm=email
	to_us=[settings.EMAIL_HOST_USER]
	send_mail(sub,msg,frm,to_us,fail_silently=False)
        messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
        return TemplateResponse(request, 'listing_tour.html',{"thanks":"Thank You For your Interest"})
    if request.method == "GET" and 'search' in request.GET:
        print request.GET
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            model_results = Iternary.objects.filter(name__contains = value)
            if len(model_results)==0:
                return TemplateResponse(request, 'listing_tour.html',{"noresult":"No Result Found"})
            else:
                return TemplateResponse(request, 'listing_tour.html',{"searchs":model_results})


    errors={}

    context={}
    if not tour_id:
        place=Places.objects.all()
        
        iternaries=Iternary.objects.filter(place=place)
        context["place"]=place
        context["iternaries"]=iternaries
        if request.method=='GET' and 'planmybutton' in request.GET:
            data= request.GET
            #print data
            name = data['name1']
            email=data['email1']
            to =data['to1']
            fr=data['fr1']  
            date=data['date1']      
            mode_of_transport=data['mode_of_tranport1']
            no_of_passenger=data['no_of_passenger1']
            discount_criteria=data['discount_criteria1']
            phone=request.GET['phone1']
            #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
            obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	    fr=fr,mode_of_transport=mode_of_transport,
	    no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
            obj.save()
            sub="[Plan My Trip] Mail From Royal Trip Maker"
	    msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
            return TemplateResponse(request, 'listing_tour.html',{"thanks":"Thank You For your Interest"})
        if request.method=='POST' and 'submitbutton' in request.POST:
            name = request.POST['name']
            email = request.POST['email']
            phone =request.POST['phone']
            comment=request.POST['comment']
            if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
                errors['fields']="Please All Fields A Required "  
            match_exists = re.match("[a-zA-Z0-9]", name)
            if(len(name)<=2):
                errors['name']="minimum length is atleast 4 characters"
            elif(match_exists==None):
               errors['name']="Only letters number _ . - are allowed"
            match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
            if(len(email)==0):
                errors['email']="Please enter email address"
            elif(match_exists==None):
                errors['email']="Please provide valid email address"
	    match_exists = re.match("\d{10,20}$", phone)
	    if len(phone)==0:
                errors['phone']="please enter phone "
	    elif(match_exists==None):
                errors['phone']= "Please provide valid Phone no.only nimber are allowed"
            if errors:
                errors=errors
                messages.error(request, 'Please fill all the correctly once again.')
            else:
	        errors={}
                #print name,email,phone,comment
                obj=Enquiry(name=name,email=email,mobile=phone,comment=comment,date=datetime.now())
                obj.save()
                sub="Mail From Royal Trip Maker"
	        msg='From : %s  \n Message : %s'%((email+"   "+"Name :"+name+" "+"Mobile:"+phone),comment)
	        frm=email
	        to_us=[settings.EMAIL_HOST_USER]
	        send_mail(sub,msg,frm,to_us,fail_silently=False)
                messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
          
    else:
        place=Places.objects.get(url_property=request.get_full_path())
        
        iternaries=Iternary.objects.filter(place=place)
        context["place"]=place
        context["iternaries"]=iternaries
        if request.method=='GET' and 'planmybutton' in request.GET:
            data= request.GET
            #print data
            name = data['name1']
            email=data['email1']
            to =data['to1']
            fr=data['fr1']  
            date=data['date1']      
            mode_of_transport=data['mode_of_tranport1']
            no_of_passenger=data['no_of_passenger1']
            discount_criteria=data['discount_criteria1']
            phone=request.GET['phone1']
            #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
            obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	    fr=fr,mode_of_transport=mode_of_transport,
	    no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
            obj.save()
            sub="[Plan My Trip] Mail From Royal Trip Maker"
	    msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
            return TemplateResponse(request, 'listing_tour.html',{"thanks":"Thank You For your Interest"})
        if request.method=='POST' and 'submitbutton' in request.POST:
            name = request.POST['name']
            email = request.POST['email']
            phone =request.POST['phone']
            comment=request.POST['comment']
            if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
                errors['fields']="Please All Fields A Required "  
            match_exists = re.match("[a-zA-Z0-9]", name)
            if(len(name)<=2):
                errors['name']="minimum length is atleast 4 characters"
            elif(match_exists==None):
                errors['name']="Only letters number _ . - are allowed"
            match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
            if(len(email)==0):
                errors['email']="Please enter email address"
            elif(match_exists==None):
                errors['email']="Please provide valid email address"
	    match_exists = re.match("\d{10,20}$", phone)
	    if len(phone)==0:
                errors['phone']="please enter phone "
	    elif(match_exists==None):
                errors['phone']= "Please provide valid Phone no.only nimber are allowed"
            if errors:
                errors=errors
                messages.error(request, 'Please fill all the correctly once again.')
            else:
	        errors={}
                #print name,email,phone,comment
                obj=Enquiry(name=name,email=email,mobile=phone,comment=comment,date=datetime.now())
                obj.save()
                sub="Mail From Royal Trip Maker"
	        msg='From : %s  \n Message : %s'%((email+"   "+"Name :"+name+" "+"Mobile:"+phone),comment)
	        frm=email
	        to_us=[settings.EMAIL_HOST_USER]
	        send_mail(sub,msg,frm,to_us,fail_silently=False)
                messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
          

    return TemplateResponse(request, 'listing_tour.html', context)

def theme_tour(request,theme_id=None):
    if request.method=='GET' and 'planmybutton' in request.GET:
        data= request.GET
        #print data
        name = data['name1']
        email=data['email1']
        to =data['to1']
        fr=data['fr1']  
        date=data['date1']      
        mode_of_transport=data['mode_of_tranport1']
        no_of_passenger=data['no_of_passenger1']
        discount_criteria=data['discount_criteria1']
        phone=request.GET['phone1']
        #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
        obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	fr=fr,mode_of_transport=mode_of_transport,
	no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
        obj.save()
        sub="[Plan My Trip] Mail From Royal Trip Maker"
	msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	frm=email
	to_us=[settings.EMAIL_HOST_USER]
	send_mail(sub,msg,frm,to_us,fail_silently=False)
        messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    if request.method == "GET" and 'search' in request.GET:
        print request.GET
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            model_results = Iternary.objects.filter(name__contains = value)
            if len(model_results)==0:
                return TemplateResponse(request, 'listing_tour.html',{"noresult":"No Result Found"})
            else:
                return TemplateResponse(request, 'listing_tour.html',{"searchs":model_results})
    context={}
    context["head"]="Top Themes"
    place=Themes.objects.get(url_property=request.get_full_path())
    
    #context["it"]=it
    context["place"]=place
    context["iternaries"]=[e for e in place.iternaries.iterator()]
    return TemplateResponse(request, 'listing_tour.html', context)

    
def vip_access(request):
    if request.method=='GET' and 'planmybutton' in request.GET:
        data= request.GET
        #print data
        name = data['name1']
        email=data['email1']
        to =data['to1']
        fr=data['fr1']  
        date=data['date1']      
        mode_of_transport=data['mode_of_tranport1']
        no_of_passenger=data['no_of_passenger1']
        discount_criteria=data['discount_criteria1']
        phone=request.GET['phone1']
        #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
        obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	fr=fr,mode_of_transport=mode_of_transport,
	no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
        obj.save()
        sub="[Plan My Trip] Mail From Royal Trip Maker"
	msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	frm=email
	to_us=[settings.EMAIL_HOST_USER]
	send_mail(sub,msg,frm,to_us,fail_silently=False)
        messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    if request.method == "GET" and 'search' in request.GET:
        print request.GET
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            model_results = Iternary.objects.filter(name__contains = value)
            if len(model_results)==0:
                return TemplateResponse(request, 'listing_tour.html',{"noresult":"No Result Found"})
            else:
                return TemplateResponse(request, 'listing_tour.html',{"searchs":model_results})

    errors={}
    if request.method=='POST' and 'vipbutton' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone =request.POST['phone']
        comment=request.POST['comment']
        print name,email,phone,comment
        if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
            errors['fields']="Please All Fields A Required "  
        match_exists = re.match("[a-zA-Z0-9]", name)
        if(len(name)<=2):
            errors['name']="minimum length is atleast 4 characters"
        elif(match_exists==None):
            errors['name']="Only letters number _ . - are allowed"
        match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
        if(len(email)==0):
            errors['email']="Please enter email address"
        elif(match_exists==None):
            errors['email']="Please provide valid email address"
	match_exists = re.match("\d{10,20}$", phone)
	if len(phone)==0:
            errors['phone']="please enter phone "
	elif(match_exists==None):
            errors['phone']= "Please provide valid Phone no.only nimber are allowed"
        if errors:
            errors=errors
            messages.error(request, 'Please fill all the correctly once again.')
        else:
	    errors={}
            obj=VipAccess(name=name,email=email,mobile=phone,comment=comment,date=datetime.now())
            obj.save()
            sub="Mail From Royal Trip Maker"
	    msg='From : %s  \n Message : %s'%((email+"   "+"Name :"+name+" "+"Mobile:"+phone),comment)
	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')

    if request.method=='POST' and 'submitbutton' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone =request.POST['phone']
        comment=request.POST['comment']
        if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
            errors['fields']="Please All Fields A Required "  
        match_exists = re.match("[a-zA-Z0-9]", name)
        if(len(name)<=2):
            errors['name']="minimum length is atleast 4 characters"
        elif(match_exists==None):
            errors['name']="Only letters number _ . - are allowed"
        match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
        if(len(email)==0):
            errors['email']="Please enter email address"
        elif(match_exists==None):
            errors['email']="Please provide valid email address"
	match_exists = re.match("\d{10,20}$", phone)
	if len(phone)==0:
            errors['phone']="please enter phone "
	elif(match_exists==None):
            errors['phone']= "Please provide valid Phone no.only nimber are allowed"
        if errors:
            errors=errors
            messages.error(request, 'Please fill all the correctly once again.')
        else:
	    errors={}
            #print name,email,phone,comment
            obj=Enquiry(name=name,email=email,mobile=phone,comment=comment,date=datetime.now())
            obj.save()
            sub="Mail From Royal Trip Maker"
	    msg='From : %s  \n Message : %s'%((email+"   "+"Name :"+name+" "+"Mobile:"+phone),comment)
	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
          
    return TemplateResponse(request, 'vip_access.html', {"nav":"vip_access"})
    
    
def low_price_guaranteed(request):
    if request.method=='GET' and 'planmybutton' in request.GET:
        data= request.GET
        #print data
        name = data['name1']
        email=data['email1']
        to =data['to1']
        fr=data['fr1']  
        date=data['date1']      
        mode_of_transport=data['mode_of_tranport1']
        no_of_passenger=data['no_of_passenger1']
        discount_criteria=data['discount_criteria1']
        phone=request.GET['phone1']
        #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
        obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	fr=fr,mode_of_transport=mode_of_transport,
	no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
        obj.save()
        sub="[Plan My Trip] Mail From Royal Trip Maker"
	msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	frm=email
	to_us=[settings.EMAIL_HOST_USER]
	send_mail(sub,msg,frm,to_us,fail_silently=False)
        messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    if request.method == "GET" and 'search' in request.GET:
        print request.GET
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            model_results = Iternary.objects.filter(name__contains = value)
            if len(model_results)==0:
                return TemplateResponse(request, 'listing_tour.html',{"noresult":"No Result Found"})
            else:
                return TemplateResponse(request, 'listing_tour.html',{"searchs":model_results})

    errors={}
    if request.method=='POST' and 'submitbutton' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone =request.POST['phone']
        comment=request.POST['comment']
        if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
            errors['fields']="Please All Fields A Required "  
        match_exists = re.match("[a-zA-Z0-9]", name)
        if(len(name)<=2):
            errors['name']="minimum length is atleast 4 characters"
        elif(match_exists==None):
            errors['name']="Only letters number _ . - are allowed"
        match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
        if(len(email)==0):
            errors['email']="Please enter email address"
        elif(match_exists==None):
            errors['email']="Please provide valid email address"
	match_exists = re.match("\d{10,20}$", phone)
	if len(phone)==0:
            errors['phone']="please enter phone "
	elif(match_exists==None):
            errors['phone']= "Please provide valid Phone no.only nimber are allowed"
        if errors:
            errors=errors
            messages.error(request, 'Please fill all the correctly once again.')
        else:
	    errors={}
            #print name,email,phone,comment
            obj=Enquiry(name=name,email=email,mobile=phone,comment=comment,date=datetime.now())
            obj.save()
            sub="Mail From Royal Trip Maker"
	    msg='From : %s  \n Message : %s'%((email+"   "+"Name :"+name+" "+"Mobile:"+phone),comment)
	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
          
    return TemplateResponse(request, 'low_price_guaranteed.html', {"nav":"low_price_guaranteed"})


def sitemap(request):
    return TemplateResponse(request,'sitemap.xml', content_type='text/xml')






def iternary_detail(request,iternary_id):

    if request.method == "GET" and 'search' in request.GET:
        print request.GET
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            model_results = Iternary.objects.filter(name__contains = value)
            if len(model_results)==0:
                return TemplateResponse(request, 'listing_tour.html',{"noresult":"No Result Found"})
            else:
                return TemplateResponse(request, 'listing_tour.html',{"searchs":model_results})
    errors={}
    if request.method=='GET' and 'planmybutton' in request.GET:
        data= request.GET
        #print data
        name = data['name1']
        email=data['email1']
        to =data['to1']
        fr=data['fr1']  
        date=data['date1']      
        mode_of_transport=data['mode_of_tranport1']
        no_of_passenger=data['no_of_passenger1']
        discount_criteria=data['discount_criteria1']
        phone=request.GET['phone1']
        #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
        obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	fr=fr,mode_of_transport=mode_of_transport,
	no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
        obj.save()
        sub="[Plan My Trip] Mail From Royal Trip Maker"
	msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	frm=email
	to_us=[settings.EMAIL_HOST_USER]
	send_mail(sub,msg,frm,to_us,fail_silently=False)
        messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
        return TemplateResponse(request, 'listing_tour.html',{"thanks":"Thank You For your Interest"})
    iternary=Iternary.objects.get(url_property=request.get_full_path())
    if request.method=='POST' and 'submitbutton' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone =request.POST['phone']
        comment=request.POST['comment']
        if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
            errors['fields']="Please All Fields A Required "  
        match_exists = re.match("[a-zA-Z0-9]", name)
        if(len(name)<=2):
            errors['name']="minimum length is atleast 4 characters"
        elif(match_exists==None):
            errors['name']="Only letters number _ . - are allowed"
        match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
        if(len(email)==0):
            errors['email']="Please enter email address"
        elif(match_exists==None):
            errors['email']="Please provide valid email address"
	match_exists = re.match("\d{10,20}$", phone)
	if len(phone)==0:
            errors['phone']="please enter phone "
	elif(match_exists==None):
            errors['phone']= "Please provide valid Phone no.only nimber are allowed"
        if errors:
            errors=errors
            messages.error(request, 'Please fill all the correctly once again.')
        else:
	    errors={}
            #print name,email,phone,comment
            obj=Enquiry(name=name,email=email,mobile=phone,comment=comment,date=datetime.now())
            obj.save()
            sub="Mail From Royal Trip Maker"
	    msg='From : %s  \n Message : %s'%((email+"   "+"Name :"+name+" "+"Mobile:"+phone),comment)
	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    if request.method=='POST' and 'iternarysubmit' in request.POST:
        name = request.POST['name']
        iternaryenquiry = request.POST['iternaryname']
        email = request.POST['email']
        phone =request.POST['phone']
        comment=request.POST['comment']
        #print name,email,phone,comment
        if len(name)==0 or len(email)==0 or len(phone)==0 or len(comment)==0:
            errors['fields']="Please All Fields A Required "  
        match_exists = re.match("[a-zA-Z0-9]", name)
        if(len(name)<=2):
            errors['name']="minimum length is atleast 4 characters"
        elif(match_exists==None):
            errors['name']="Only letters number _ . - are allowed"
        match_exists = re.match("[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)", email)
        if(len(email)==0):
            errors['email']="Please enter email address"
        elif(match_exists==None):
            errors['email']="Please provide valid email address"
	match_exists = re.match("\d{10,20}$", phone)
	if len(phone)==0:
            errors['phone']="please enter phone "
	elif(match_exists==None):
            errors['phone']= "Please provide valid Phone no.only nimber are allowed"
        if errors:
            errors=errors
            messages.error(request, 'Please fill all the correctly once again.')
        else:
	    errors={}
            obj=IternaryEnquiry(name=name,email=email,iternaryenquiry=iternaryenquiry,
            mobile=phone,comment=comment,date=datetime.now())
            obj.save()
            sub="Mail From Royal Trip Maker"
	    msg='From : %s \n Name: %s \n Phone No: %s \n Enquiry For: %s \n Messag: %s'%(email,name,phone,iternaryenquiry,comment)

	    frm=email
	    to_us=[settings.EMAIL_HOST_USER]
	    send_mail(sub,msg,frm,to_us,fail_silently=False)
            messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
    if request.method=='GET' and 'planmybutton' in request.GET:
        data= request.GET
        #print data
        name = data['name1']
        email=data['email1']
        to =data['to1']
        fr=data['fr1']  
        date=data['date1']      
        mode_of_transport=data['mode_of_tranport1']
        no_of_passenger=data['no_of_passenger1']
        discount_criteria=data['discount_criteria1']
        phone=request.GET['phone1']
        #print name,email,to,fr,date,mode_of_tranport,discount_criteria,mobile
        obj=PlanMyTrip(name=name,email=email,mobile=phone,to=to,date=date,
	fr=fr,mode_of_transport=mode_of_transport,
	no_of_passenger=no_of_passenger,discount_criteria=discount_criteria)
        obj.save()
        sub="[Plan My Trip] Mail From Royal Trip Maker"
	msg='From : %s  \n Name : %s\n Phone :%s\n To :%s \n From :%s \n Date :%s\n Mode Of Transport :%s\n No Of Passenger :%s \n Discount Criteria :%s'%(email,name,phone,to,fr,date,mode_of_transport,no_of_passenger,discount_criteria)
	frm=email
	to_us=[settings.EMAIL_HOST_USER]
	send_mail(sub,msg,frm,to_us,fail_silently=False)
        messages.success(request, 'Message sent successfully you will recieve a phone call shortly.')
        return TemplateResponse(request, 'listing_tour.html',{"thanks":"Thank You For your Interest"})  
    
    return TemplateResponse(request, 'details.html', {"gallery":GalleryImages.objects.filter(place=iternary),"iternary":iternary})


def nearest_buses(request):
    #/api/bus_stops/?lat=18.940708&long=72.833214
    lat=request.GET.get("lat")
    longi=request.GET.get("long")
    dist=request.GET.get("dist")
    if dist:
        try:
            dist=float(dist)
        except:
            dist=None
    if not (lat and longi):
        
        return JsonResponse({"error":"lat , long required"})
    try:
        pos=[float(lat) , float(longi)]
    except:
        return JsonResponse({"error":"lat , long invalid"})
    
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)
    from bson.son import SON
    db=client.bestpis # Create db name best
    bus_stops = db.bus_stops
    if not dist:
        dist=0.005
    query = {"latlong": SON([("$near", pos), ("$maxDistance", dist)])}
    #query= {"latlong":SON([("$geoWithin", pos), ("$maxDistance", dist)])} 
    #http://stackoverflow.com/questions/17415192/how-to-use-geowithin-in-mongodb
    #{"adr.cor":{"$geoWithin":{"$center":[center, perim]}}}
    #http://stackoverflow.com/questions/21642213/geowithin-center-with-pymongo-aggregation-throws-error
    #{'location' : {'$geoWithin': {'$centerSphere': [[lng,lat], distance] }
    #query={'location' : {'$geoWithin': {'$centerSphere': [[-88,30], 1000000000000000000000000/3963.2] }}}
    #query={"latlong":{"$near":[18.940708,72.833214], "e": 5 }}
    records= bus_stops.find(query)        
    #{ $geoWithin: { $centerSphere: [ [ -88, 30 ], 10/3963.2 ] } }} 
    
    records=[e for e in records]
    dd={}
    ll=[]
    for record in records:
        
        if (record['latlong'][0],record['latlong'][1]) not in dd:
#             ll.append({"stop_name":str(record['stopname']),
#                        "lat":record['latlong'][0],
#                        "long":record['latlong'][1],
#                        "depot":str(record['depot']),
#                        "road_name":str(record["road_name"]),
#                        "stop_code":str(record["stop_code"]),
#                        "direction":str(record["u'direction"]) # DN,"UP"
#                        
#                        })
            try:
                ll.append({"line1":str(record['stopname']) + "("+str( record["stopcode"]) +")",
                           "line2":"",
                           "line3":str(record["road_name"]),
                           "line4":"Depot : "+str(record["depot"]) + "("+str(record["direction"])+")",
                           "lat":record['latlong'][0],
                           "long":record['latlong'][1],
                           "stop_name":str(record['stopname']),
                           "stop_code":str(record["stopcode"]),
                           
                           
                           })
            except:
                import pdb;pdb.set_trace()
            
            dd[(record['latlong'][0],record['latlong'][1])]=1 
        else:
            print record['latlong'][0],record['latlong'][1] ,record['stopname'] , "Repeated "
             
          

                
    #response= {"status":"success","bus_stops":ll}
    response= {"status":"success","bus_stops":ll}
    return JsonResponse(response)
    



       




