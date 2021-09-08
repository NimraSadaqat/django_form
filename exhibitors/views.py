from django.shortcuts import render
from .models import Exhibitor
from events_venue.models import Event
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'exhibitors/form1.html')

def multistepform1_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("exhibitors:main-view"))
    else:
        email = request.POST.get("email")

        event = Event.objects.filter(exhibitor_creator_list = email)
        print(event)
        if event:
            if event[0].status == "Complete":
                return render(request, 'exhibitors/event_details.html',{'obj':event[0]})
            if event[0].status == "InProgress":
                return render(request, 'exhibitors/form2.html',{'email':email,
                                                                'event':event[0]})
            else:
                messages.error(request,"Sorry Event status is Error, Exhibitor can not be created!")
                return HttpResponseRedirect(reverse('exhibitors:thanks'))
        else:
            messages.error(request,"Sorry No record found, Exhibitor can not be created!")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))

def multistepform2_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("exhibitors:main-view"))
    else:
        email = request.POST.get("email")
        name = request.POST.get("name")
        brand_name = request.POST.get("brand_name")
        name_incharge = request.POST.get("name_incharge")
        designation_incharge = request.POST.get("designation_incharge")
        exhibitor_page_link = request.POST.get("exhibitor_page_link")
        exhibitor_website = request.POST.get("exhibitor_website")
        exhibitor_email = request.POST.get("exhibitor_email")
        exhibitor_both_number = request.POST.get("exhibitor_both_number")
        exhibitor_city = request.POST.get("exhibitor_city")
        exhibitor_country = request.POST.get("exhibitor_country")
        exhibitor_address = request.POST.get("exhibitor_address")
        type = request.POST.get("type")
        exhibitor_product = request.POST.get("exhibitor_product")
        linkedin = request.POST.get("linkedin")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        instagram = request.POST.get("instagram")
        youtube = request.POST.get("youtube")
        tiktok = request.POST.get("tiktok")
        hashtag = request.POST.get("hashtag")
        mention = request.POST.get("mention")
        description = request.POST.get("description")
        logo = request.POST.get("logo")

        try:
            Exhibitor.objects.create(
            email = email,
            name = name,
            brand_name = brand_name,
            name_incharge = name_incharge,
            designation_incharge = designation_incharge,
            exhibitor_page_link = exhibitor_page_link,
            exhibitor_website = exhibitor_website,
            exhibitor_email = exhibitor_email,
            exhibitor_both_number = exhibitor_both_number,
            exhibitor_city = exhibitor_city,
            exhibitor_country = exhibitor_country,
            exhibitor_address = exhibitor_address,
            type = type,
            exhibitor_product = exhibitor_product,
            linkedin = linkedin,
            twitter = twitter,
            facebook = facebook,
            instagram = instagram,
            youtube = youtube,
            tiktok = tiktok,
            hashtag = hashtag,
            mention = mention,
            description = description,
            logo = logo
            )
            messages.success(request,"Exhibitor Saved Successfully, Thank you.")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))
        except:
            messages.error(request,"Error in Saving Exhibitor")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))

def response_recorded(request):
    return render(request, 'exhibitors/thanks.html')

def event_details(request):
    return render(request, 'exhibitors/event_details.html')
