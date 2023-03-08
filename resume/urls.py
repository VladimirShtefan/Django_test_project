from django.urls import path

from resume.views import UserResumeView

urlpatterns = [
    path('resume/<int:pk>', UserResumeView.as_view(), name='user_resume'),
]
