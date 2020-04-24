from django.shortcuts import render
from .Excel import bd1
from .Excel2 import bd2


# Create your views here.

def homepage(request):
    return render(request, 'bin/index.html', {'cont2': bd1, 'cont': bd2})
