from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'mypage/index.html')
    
def consumer(request):
    return render(request, 'mypage/consumer.html')
    
def merchants_area(request):
    return render(request, 'mypage/merchants_area.html')
    
def vendors_area(request):
    return render(request, 'mypage/vendors_area.html')
