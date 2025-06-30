from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request, 'website/index.html')
    # return HttpResponse("Hello, world! This is the home page of the coffeeProject.")
  
def about(request):
  return render(request, 'website/about.html')
    # return HttpResponse("This is the about page of the coffeeProject. Here you can learn more about our project and its features.")

def contact(request):
  return render(request, 'website/contact.html')
    # return HttpResponse("This is the contact page of the coffeeProject. You can reach us at")