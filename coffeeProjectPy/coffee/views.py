from django.shortcuts import render
from .models import CoffeeVariety, Store
from django.shortcuts import get_object_or_404
from .forms import CoffeeStoreForm
 
# Create your views here.
def all_coffee(request):
    coffees = CoffeeVariety.objects.all()
    return render(request, 'coffee/all_coffee.html', {'coffees': coffees})

def coffee_detail(request, coffee_id):
    coffee = get_object_or_404(CoffeeVariety, id=coffee_id)
    
    return render(request, 'coffee/coffee_detail.html', {'coffee': coffee})

def coffee_store_view(request):
    stores = None
    if request.method == 'POST':
        form = CoffeeStoreForm(request.POST)
        if form.is_valid():
            coffee_veriety = form.cleaned_data['coffee_variety']
            stores = Store.objects.filter(coffee_varieties=coffee_veriety)
        else:
            form = CoffeeStoreForm()
    else:
        form = CoffeeStoreForm()
    return render(request, 'coffee/coffee_stores.html', {'form': form, 'stores': stores})