import pytest
from django.urls import reverse
from rest_framework import status

from resume.serializers import UserResumeSerializer


@pytest.mark.django_db
class TestGetResume:
    def test_get_resume(self, resume_factory, api_client):
        resume = resume_factory.create()
        url = reverse('user_resume', args=(resume.id,))
        api_client.force_login(resume.user)
        response = api_client.get(url)
        api_client.logout()
        response_another_user = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response_another_user.status_code == status.HTTP_200_OK
        assert response.data == UserResumeSerializer(resume).data
        assert response_another_user.data == UserResumeSerializer(resume).data

    def test_patch_resume(self, resume_factory, api_client, user_factory):
        resume = resume_factory.create()
        api_client.force_login(resume.user)
        url = reverse('user_resume', args=(resume.id,))
        response = api_client.patch(url, {"grade": 5000})
        assert response.status_code == status.HTTP_200_OK
        resume.grade = 5000
        assert response.data == UserResumeSerializer(resume).data
        user = user_factory.create()
        api_client.force_login(user)
        response_another_user = api_client.patch(url, {"grade": 5000})
        assert response_another_user.status_code == status.HTTP_403_FORBIDDEN
