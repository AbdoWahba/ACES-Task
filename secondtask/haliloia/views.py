from django.shortcuts import render
from django.http import HttpResponse
from haliloia import models



# Create your views here.
def About(request):
    abouts=models.About.objects.all()
    context={
              'abouts':abouts
            }
    return render(request,'FirstTask.html',context)