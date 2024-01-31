from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('subscribtion/',views.subscribtion),
    path('about/',views.about),
    path('enquiry/',views.enquiry),
    path('contact/',views.contact),
    path('website/',views.website),
    path('graphic-designing/',views.graphicDesigning),
    path('digital-marketing/',views.digitalMarketing),
    path('seo/',views.seo),
    path('paid-advertising/',views.paidAdvertising),
    path('digital-pr/',views.digitalPr),
    path('social-media/',views.socialMedia),
    path('email-marketing/',views.emailMarketing),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
