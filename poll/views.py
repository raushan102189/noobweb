from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from poll.models import User

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        gender = request.POST.get('gender')
        additonal_number = request.POST.get('num')

        new = User(name=name,email=email,number=number,gender=gender,additonal_number=additonal_number)

        new.save()
     



        # return HttpResponse("You're name is  %s." %new.name )
        return render(request,'details.html')
    
       
   
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the poll index.")
# Create your views here.
# def detail(request):
#     return Htt=
def about(request):
    return HttpResponse("Hello, world. You're at the poll about.")