from django.contrib import admin
from django.urls import path

from adoptions import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adoptions/<int:id>/', views.pet_details, name='pet_detail'),
]
