from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Captain(request):
    return HttpResponse("<h1 style=color:red;background-color:black;padding:20px;text-align:center;font-weight:600;><marquee>King Kohli is Greatest of all time of the Cricket</marquee></h1>")