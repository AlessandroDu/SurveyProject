from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_survey/", views.create_survey, name="create_survey"),
    path("submit_survey/<int:survey_id>/", views.submit_survey, name="submit_survey"),
    path("view_submissions/<int:survey_id>/", views.view_submissions, name="view_submissions"),
]