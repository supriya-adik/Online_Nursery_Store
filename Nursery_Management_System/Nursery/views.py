from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import Add_Plant_Form,CustomerForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
# Create your views here.


def index(request) :
    return render(request,'Nursery/index.html')

@login_required
def add_plant_func(request) :
    form = Add_Plant_Form()
    lastimage = Add_plant.objects.last()
    imagefile = lastimage.imagefile;
    if request.method == "POST" :
        form = Add_Plant_Form(request.POST or None,request.FILES or None)
        if form.is_valid() :
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'Nursery/add_plant.html',context=context)

@login_required()
def show_plant_func(request) :
    obj = Add_plant.objects.all()
    return render(request,'Nursery/show_plant.html',{'images':obj})

@login_required()
def all_plant_func(request) :
    obj = Add_plant.objects.all()
    return render(request,'Nursery/all_plant.html',{'images':obj})

@login_required()
def all_plant_types(request) :
    return render(request,'Nursery/all_types.html')

@login_required()
def vegetable_plants(request) :
    veg = Add_plant.objects.filter(plant_type='Vegetable')
    return render(request, 'Nursery/veg_plant.html', {'veg': veg})

@login_required()
def flowering_plants(request) :
    flower = Add_plant.objects.filter(plant_type='Flowering')
    return render(request, 'Nursery/flower_plant.html', {'flower': flower})

def logout_user(request) :
    logout(request)
    return render(request,'Nursery/logout.html')


def register(request) :
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid() :
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('../accounts/login')
    return render(request, 'Nursery/register.html', {'form':form})

@login_required()
def profile(request):
            current_user =request.user
            return render(request, "Nursery/profile.html", {'user':current_user})

@login_required()
def plant_order_by_customer(request) :
    form = CustomerForm()
    total = 0
    #request.session.flush()
    if request.method=="POST":
        plant = Add_plant.objects.all()
        id = request.POST.get('plant_name')
        print(id)

        qty = request.POST.get('qty')
        print(qty)

        pn = Add_plant.objects.get(id=id)
        price = pn.price

        plant_name = pn.plant_name
        print("price:", price)

        total = int(qty) * int(price)
        print("total:", total)

        # pname = plant_add.objects.values_list('plant_name')
        # print(pname)
        # for i in pname:
        # print(i)

        request.session['total'] = total
        request.session['price'] = price
        request.session['qty'] = qty
        request.session['plant'] = plant_name

        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/my_order')
    return render(request, 'Nursery/order_plant.html',{'form':form})

def my_order_plant(request) :

    current_user = request.user
    plant_name = request.session['plant']
    total=request.session['total']
    price=request.session['price']
    qty = request.session['qty']

    #form = JournalForm(initial={'tank': 123})

    #my_plant = order_plant1.objects.filter(Customer_Name=current_user.username)

    return  render(request,'Nursery/my_order.html',{'name':current_user.username,'qty':qty,'plant_name':plant_name,'total':total,'price':price})

@login_required()
def order_details(request) :
    current_user =request.user
    my_plant = order_plant1.objects.filter(Customer_Name=current_user.username)
    return render(request, 'Nursery/order_details.html', {'form': my_plant,'user':current_user.username})


@login_required()
def update_plant(request,id) :
    context = {}
    obj = get_object_or_404(Add_plant,id=id)
    form =Add_Plant_Form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/show_plant")
    context["form"] = form
    return render(request, "Nursery/update_plant.html", context)

@login_required()
def delete_plant(request,id):
	context={}
	obj=get_object_or_404(Add_plant,id=id)
	if request.method=="POST" :
		obj.delete()
		return HttpResponseRedirect("/show_plant")

	return render(request,"Nursery/delete_plant.html",context)
