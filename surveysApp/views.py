from django.shortcuts import render, redirect, get_object_or_404
from .models import Survey, Question, Option, Submission, Answer
from .forms import QuestionForm, OptionForm

def home(request):
    surveys = Survey.objects.all()
    return render(request, "surveysApp/home.html", {"surveys": surveys})

def create_survey(request):
    if request.method == 'POST':
        survey_title = request.POST.get('survey_title')
        survey_description = request.POST.get('survey_description')
        survey = Survey.objects.create(title=survey_title, description=survey_description)

        # Add questions dynamically
        for i in range(int(request.POST.get('question_count', 0))):
            question_text = request.POST.get(f'question_text_{i}')
            question_type = request.POST.get(f'question_type_{i}')
            question = Question.objects.create(survey=survey, question=question_text, type=question_type)

            # Add options if it's a multiple-choice question
            if question_type == 'multiple_choice':  # Make sure to match your model's field name
                option_count = int(request.POST.get(f'option_count_{i}', 0))
                for j in range(option_count):
                    option_text = request.POST.get(f'option_text_{i}_{j}')
                    Option.objects.create(question=question, optionText=option_text)  # Matching field name here

        return redirect('surveysApp/home.html')

    return render(request, 'surveysApp/create_survey.html')


# View for submitting a survey
def submit_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    
    if request.method == 'POST':
        # Create a new submission
        submission = Submission.objects.create(survey=survey, user=request.user)  # Optional user field

        # Process the submitted answers
        for question in survey.questions.all():
            answer_text = request.POST.get(f"answer_{question.id}")
            if question.type == 'open':  # Matching your model's type for open-ended questions
                Answer.objects.create(
                    submission=submission,
                    question=question,
                    text=answer_text
                )
            elif question.type == 'multiple_choice':  # For multiple-choice questions
                selected_option_id = request.POST.get(f"answer_{question.id}")
                selected_option = Option.objects.get(id=selected_option_id)
                Answer.objects.create(
                    submission=submission,
                    question=question,
                    selected_option=selected_option
                )
        return redirect('survey_thank_you')  # Redirect after submission
    
    return render(request, 'surveysApp/submit_survey.html', {'survey': survey})

# View for displaying submissions
def view_submissions(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    submissions = Submission.objects.filter(survey=survey)
    
    return render(request, 'surveysApp/view_submissions.html', {
        'survey': survey,
        'submissions': submissions,
    })
