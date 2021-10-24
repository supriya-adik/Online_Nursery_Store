from django import forms
from .models import Add_plant,order_plant1
from django import forms
from django.contrib.auth.models import User
from  django.contrib.auth.forms import UserCreationForm

class Add_Plant_Form(forms.ModelForm) :
    class Meta :
        model = Add_plant
        fields = '__all__'



from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class CustomerForm(forms.ModelForm) :

    class Meta :
        model = order_plant1
        fields='__all__'
