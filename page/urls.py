from.import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [


path('',views.home,name='home'),
path('about',views.about,name='about'),

path('contact',views.contact,name='contact')

] 

urlpatterns += staticfiles_urlpatterns()