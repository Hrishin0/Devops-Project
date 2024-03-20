from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dog',views.show, name="show"),
    path('addpet/', views.addpet, name='addpet'),
    path('update/<pet_id>', views.update, name='update'),
]
# to access dog you would go to sign/dog 