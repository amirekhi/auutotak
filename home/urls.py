from django.urls import path
from . import views


urlpatterns = [
    path('' , views.index , name='home'),
    path('cars' , views.cars , name='cars'),
    path('about' , views.about1 , name='about'),
    path('contact' , views.contact , name='contact'),
    path('car_pic/<int:car_id>' , views.car_pic , name='car_pic'),
]