from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dog',views.show, name="show"),
    path('addpet/', views.addpet, name='addpet'),
    path('details/<petid>', views.details, name='details'),
    path('update/<petid>', views.update, name='update'),
    path('delete/<petid>',views.delete, name='delete'),
]
# to access dog you would go to pet/dog 