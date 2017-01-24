from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def index(request):
    return render(request, 'Webapp/Home.html')

#def naivebayes(request):
 #   return render(request, 'webapp/UserForm.html')

def Submit(request):
    return  render(request, 'webapp/Result.html')
def aboutus(request):
    return  render(request, 'Webapp/About.html')
def contactus(request):
    return  render(request, 'Webapp/Contactus.html')
def home(request):
    return  render(request, 'Webapp/Home.html')

