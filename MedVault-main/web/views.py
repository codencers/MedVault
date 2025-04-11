from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pyzbar.pyzbar import decode
from PIL import Image


# Create your views here.
def index(request):
    return render(request, 'try.html')

def doc(request):
    return render(request, 'doctor.html')

def file(request):
     return render(request, "file.html")

def dashboard(request):
     return render(request, "dashboard.html")

def login(request):
     return render(request, "login.html")

def ipfs(request):
     return render(request, "ipfs.html")

def landing(request):
     return render(request, "landing.html")

def doclogin(request):
     return render(request, "doclogin.html")