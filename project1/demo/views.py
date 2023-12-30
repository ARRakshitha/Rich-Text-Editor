from .forms import StudentForm
from django.shortcuts import render
# Create your views here.

def home(request):
    form=StudentForm
    mydict={
        'form' :form
    }
    return render(request,'index.html',context=mydict)
