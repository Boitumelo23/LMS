from django.urls import path
from . import views

urlpatterns = [
    path('', views.assessmentsList, name='assessment_list'),
    path('<int:pk>/', views.assessmentsById, name='assessment_detail'),
    path('learning_unit/<int:pk>/', views.assessmentsByLearningUnit, name='learning_unit_assesssment')
   
]