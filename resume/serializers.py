from rest_framework import serializers

from resume.models import Resume


class UserResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = '__all__'
