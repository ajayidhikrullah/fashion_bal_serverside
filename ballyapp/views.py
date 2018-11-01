from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('welcome to Balqees page.')
    return render(request, 'ballyapp/index.html')
