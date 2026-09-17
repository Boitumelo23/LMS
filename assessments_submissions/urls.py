from django.urls import path
from . import views

urlpatterns = [
    path('learner/<int:pk>/', views.getSubmissionsByLearnerId, name='learner_submission'),
    path('assessment/<int:pk>/', views.getSubmissionByAssessmentId, name = 'assessment_submission')
]