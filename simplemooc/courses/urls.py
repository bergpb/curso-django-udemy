from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:id>', views.details, name='details')
    path('<str:slug>', views.details, name='details')
]
