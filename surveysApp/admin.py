from django.contrib import admin
from .models import Survey, Question, Option, Submission, Answer

# Survey Model
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Fields to show in the list view
    search_fields = ('title', 'description')  # Add search functionality
    ordering = ('title',)  # Optional: order the surveys by title in the admin

# Question Model
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'type', 'survey')  # Fields to show in the list view
    search_fields = ('question', 'type')  # Add search functionality
    list_filter = ('type',)  # Optional: filter by question type
    ordering = ('survey',)  # Optional: order the questions by survey

# Option Model (for Multiple Choice)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('optionText', 'question')  # Fields to show in the list view
    search_fields = ('optionText',)  # Add search functionality
    ordering = ('question',)  # Optional: order the options by question

# Submission Model
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'user', 'created_at')  # Fields to show in the list view
    search_fields = ('survey__title', 'user__username')  # Search by survey title and username
    list_filter = ('survey',)  # Filter submissions by survey
    ordering = ('-created_at',)  # Order by creation time in descending order

# Answer Model
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('submission', 'question', 'selected_option', 'text')  # Fields to show in the list view
    search_fields = ('submission__id', 'question__question', 'selected_option__optionText')  # Search functionality
    list_filter = ('question',)  # Filter answers by question
    ordering = ('submission',)  # Optional: order answers by submission

# Register models with custom ModelAdmin
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Answer, AnswerAdmin)
