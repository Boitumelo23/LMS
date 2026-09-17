from django.shortcuts import render
from .models import Assessments

def assessmentsList(request):
    assessments = Assessments.objects.all().order_by('created_at')
    return render(request, 'assessments/assessments.html', {'assessments': assessments})


def assessmentsById(request, id):
    try:
        assessment = Assessments.objects.get(assessment_id=id)
        return render(request, 'assessments/assessments.html', {'assessment': assessment})
    except Assessments.DoesNotExist:
        return render(request, 'assessments/assessments.html', {'error': 'Assessment not found'})


def assessmentsByLearningUnit(request, learning_unit_id):
    try:
        assessments = Assessments.objects.filter(learning_unit_id=learning_unit_id).order_by('created_at')
        return render(request, 'assessments/assessments.html', {'assessments': assessments})
    except Assessments.DoesNotExist:
        return render(request, 'assessments/assessments.html', {'error': 'No assessments found for this learning unit'})
