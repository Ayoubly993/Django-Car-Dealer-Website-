from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Car

def home(request):
    cars = Car.objects.all()[0:16]
    main_car = get_object_or_404(Car,main_car=True)
    image_car= main_car.car_images.all()[0].image.url
    



    context={
        'image_car':image_car,
        'main_car':main_car,
        'cars': cars,
    }
    return render(request,'base/index.html',context)

def contact(request):

    return render(request,'base/contact.html')


def about(request):

    return render(request,'base/contact.html')