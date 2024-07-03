from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Asvatthama Hatah! kunjovara")
    return render (request, 'home.html')

