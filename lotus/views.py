from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    data={
        'lodData':Lod.objects.all()
    }
    return render(request,'index.html', data)