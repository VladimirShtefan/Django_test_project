from rest_framework.generics import RetrieveUpdateAPIView

from resume.models import Resume
from resume.permissions import IsOwnerOrReadOnly
from resume.serializers import UserResumeSerializer


class UserResumeView(RetrieveUpdateAPIView):
    queryset = Resume.objects.all()
    serializer_class = UserResumeSerializer
    permission_classes = [IsOwnerOrReadOnly]
