from django.shortcuts import render
from app1.models import Data

# Create your views here.

def data(request):
    Dt = Data.objects.all()
    return render(request,'app2/Data.html',{'Data':Dt})

def data2(request):

    return render(request,'app2/Data2.html',)
