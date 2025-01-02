from django.db import models
from django.contrib.auth.models import User  # To associate with a user (optional)

# Survey Model
class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# Question Model
class Question(models.Model):
    QUESTION_TYPES = [
        ('open', 'Open Answer'),
        ('multiple_choice', 'Multiple Choice'),
    ]
    survey = models.ForeignKey(Survey, related_name="questions", on_delete=models.CASCADE)
    question = models.CharField(max_length=120)
    type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.question

# Option Model (for Multiple Choice)
class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    optionText = models.CharField(max_length=120)

    def __str__(self):
        return self.optionText

# Submission Model
class Submission(models.Model):
    survey = models.ForeignKey(Survey, related_name="submissions", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="submissions", on_delete=models.CASCADE, null=True, blank=True)  # Optional user field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.id} for {self.survey.title}"

# Answer Model
class Answer(models.Model):
    submission = models.ForeignKey(Submission, related_name="answers", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)  # For open-ended questions
    selected_option = models.ForeignKey(Option, null=True, blank=True, on_delete=models.CASCADE)  # For multiple-choice questions

    def __str__(self):
        if self.selected_option:
            return f"Answer for {self.question.question}: {self.selected_option.optionText}"
        return f"Answer for {self.question.question}: {self.text}"
