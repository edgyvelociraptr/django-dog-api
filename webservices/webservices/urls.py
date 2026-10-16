"""
URL configuration for webservices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from dogapi import views
from dogapi.views import rest_get_breed
from dogapi.views import rest_get_dog
from dogapi.views import DogList, DogDetail, BreedList, BreedDetail 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('rest/dog/<int:dog_id>/', rest_get_dog, name='rest_get_dog'),
    # path('rest/breed/<breed>/', rest_get_breed, name='rest_get_breed'),

    path('rest/dog/', DogList.as_view(), name='dog-list'),
    path('rest/dog/<int:pk>/', DogDetail.as_view(), name='dog-detail'),

    path('rest/breed/', BreedList.as_view(), name='breed-list'),
    path('rest/breed/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),

]
