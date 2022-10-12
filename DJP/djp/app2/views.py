from django.shortcuts import render
from app1.models import Data
from app2.models import Data2

# Create your views here.

def data(request):
    Dt = Data.objects.all()
    return render(request,'app2/Data.html',{'Data':Dt})

def data2(request):
    Dt2 = Data2.objects.all()
    return render(request,'app2/Data2.html',{"Data2":Dt2})
def about(request):
    return render(request,"app2/About.html")
