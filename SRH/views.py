from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Captain(request):
    return HttpResponse("<h1 style=color:Black;background-color:gold;padding:20px;text-align:center;font-weight:600;><marquee>Nithish Kumar reddy is a Destructive Batsman in SRH</marquee></h1>")