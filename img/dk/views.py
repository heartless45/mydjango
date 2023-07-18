from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request ,'1.html')

def a(request):
    return render(request , '2.html')