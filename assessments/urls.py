from django.urls import path
from . import views

urlpatterns = [
    path('', views.assessment_list, name='assessment_list'),
    path('<int:pk>/', views.assessment_detail, name='assessment_detail'),
   
]