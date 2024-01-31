from django.shortcuts import render,redirect
from django.contrib import messages
def home(Request):
    return render(Request,"index.html")

def subscribtion(Request):
    if(Request.method=="POST"):
        messages.success(Request,"“Subscribed Successfully”")
    return redirect("/")

def about(Request):
    return render(Request,"about.html")

def enquiry(Request):
    if(Request.method=="POST"):
        messages.success(Request,"“Your form submitted Successfully”")
    return render(Request,"enquiry.html")

def contact(Request):
    if(Request.method=="POST"):
        messages.success(Request,"“Your form submitted Successfully”")
    return render(Request,"contact.html")

def website(Request):
    return render(Request,"website.html")

def graphicDesigning(Request):
    return render(Request,"graphic-designing.html")

def digitalMarketing(Request):
    return render(Request,"digital-marketing.html")

def seo(Request):
    return render(Request,"seo.html")

def paidAdvertising(Request):
    return render(Request,"paid-advertising.html")

def digitalPr(Request):
    return render(Request,"digital-pr.html")

def socialMedia(Request):
    return render(Request,"social-media.html")

def emailMarketing(Request):
    return render(Request,"email-marketing.html")



