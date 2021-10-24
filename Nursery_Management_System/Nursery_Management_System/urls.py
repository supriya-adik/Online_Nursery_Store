"""Nursery_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Nursery import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('add_plant/',views.add_plant_func,name="add_plant_func"),
    path('show_plant/',views.show_plant_func,name="show_plant_func"),
    path('all_plant/',views.all_plant_func,name="all_plant_func"),
    path('all_types/',views.all_plant_types,name="all_plant_types"),
    path('vegetable_plants/', views.vegetable_plants, name="vegetable_plants"),
    path('flowering_plants/',views.flowering_plants,name="flowering_plants"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('order_plant/',views.plant_order_by_customer,name="plant_order_by_customer"),
    path('profile/', views.profile ,name="profile"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/',views.logout_user,name="logout_user"),
    path('my_order/',views.my_order_plant,name="my_order_plant"),
    path('update_plant/<id>',views.update_plant,name="update_plant"),
    path('delete_plant/<id>',views.delete_plant,name="delete_plant"),
    path('order_details/',views.order_details,name="order_details"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
