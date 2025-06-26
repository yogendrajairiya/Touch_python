from django.shortcuts import render

# Create your views here.
def all_touch(request):
    return render(request, 'touch/all_touch.html')