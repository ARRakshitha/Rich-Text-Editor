from django.forms import ModelForm
from .models import*



class StudentForm(ModelForm):
    class Meta:
       models = Student
       fields = '__all__'
