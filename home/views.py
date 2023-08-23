from django.shortcuts import render
from .models import Cars , about ,  Contact , Home

# Create your views here.


def index(request) :
    return render(request , 'home/index.html' , {
        'home' : Home.objects.first()
    } )



def cars(request) :
    return render(request , 'home/cars.html', {
        'cars': Cars.objects.all()
    })



def about1(request) :
    return render(request , 'home/about.html' , {
        'about':about.objects.first()
    } )



def contact(request) :
    return render(request , 'home/contact.html', {
        'contact' : Contact.objects.first()
    })


def car_pic(request , car_id) :
    car = Cars.objects.get(id = car_id)
    return render(request , 'home/index3.html' , {
        'car' : car
    })
    