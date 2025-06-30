from django.shortcuts import render
from .models import CoffeeVariety
from django.shortcuts import get_object_or_404
# Create your views here.
def all_coffee(request):
    coffees = CoffeeVariety.objects.all()
    return render(request, 'coffee/all_coffee.html', {'coffees': coffees})

def coffee_detail(request, coffee_id):
    coffee = get_object_or_404(CoffeeVariety, id=coffee_id)
    
    return render(request, 'coffee/coffee_detail.html', {'coffee': coffee})