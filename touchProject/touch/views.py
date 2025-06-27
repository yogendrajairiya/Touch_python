from django.shortcuts import render
from .models import TouchVariety
from django.shortcuts import get_object_or_404
# Create your views here.
def all_touch(request):
    touches = TouchVariety.objects.all()
    return render(request, 'touch/all_touch.html', {'touches': touches})

def touch_detail(request, touch_id):
    touch = get_object_or_404(TouchVariety, id=touch_id)
    
    return render(request, 'touch/touch_detail.html', {'touch': touch})