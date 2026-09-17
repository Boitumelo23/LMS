from django.shortcuts import render
from .models import AssessmentsSubmission


# Create your views here.
def getSubmissionsByLearnerId(request, learner_id):
        assessments_submission = AssessmentsSubmission.objects.filter(learner_id = learner_id ).order_by('submission_date')
        if not assessments_submission.exists():
             return render(
                  request,
                  'assessments_submissions/assessments_submissions.html',
                  {'error': 'Assessment submission not found'}
             )
        return render(
             request,
             'assessments_submissions/assessments_submissions.html',
             {'assessment_submission': assessments_submission}
        )

def getSubmissionByAssessmentId(request, assessment_id):
    assessment_submission = AssessmentsSubmission.objects.filter(assessment_id = assessment_id).order_by('submission_date')
    if not assessment_submission.exists():
        return render(
            request,
            'assessments_submissions/assessments_submissions.html',
            {'error': 'Assessment submission not found'}
        )
    return render(
         request, 
         'assessments_submissions/assessments_submissions.html',
         {'assessment_submission': assessment_submission})

        