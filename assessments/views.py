from django.shortcuts import render

# Create your views here.
from .models import Assessment

def assessment_list(request):
    assessments = Assessment.objects.all()
    return render(request, 'assessments/assessment_list.html', {'assessments': assessments})

def assessment_detail(request, pk):
    assessment = Assessment.objects.get(pk=pk)
    return render(request, 'assessments/assessment_detail.html', {'assessment': assessment})

