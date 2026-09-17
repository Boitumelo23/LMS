from django.shortcuts import render
from .models import Assessment

def assessmentsList(request):
    assessments = Assessment.objects.all().order_by('created_at')
    return render(
        request, 
        'assessments/assessments.html', 
        {'assessments': assessments}
        )


def assessmentsById(request, id):
    try:
        assessment = Assessment.objects.get(assessment_id=id)
        return render(
            request, 
            'assessments/assessments.html', 
            {'assessment': assessment}
            )
    except Assessment.DoesNotExist:
        return render(
            request, 
            'assessments/assessments.html', 
            {'error': 'Assessment not found'}
            )


def assessmentsByLearningUnit(request, learning_unit_id):
    assessments = Assessment.objects.filter(learning_unit_id=learning_unit_id).order_by('created_at')

    if not assessments.exists:
        return render(
            request,
            'assessments/assessments.html',
            {'error': 'Assessment not found'}
        )    
    return render(
        request,
        'assessments/assessments.html',
        {'assessments': assessments}
    )
