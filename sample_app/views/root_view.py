from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class RootView():
    def index(request):
        return HttpResponse("Hello, world.")
