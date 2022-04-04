from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def floor1(request):
    return render(request, 'floor1.html')

def floor2(request):
    return render(request, 'floor2.html')

def floor3(request):
    return render(request, 'floor3.html')