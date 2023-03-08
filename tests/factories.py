from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from pytest_factoryboy import register


@register
class UserFactory(DjangoModelFactory):
    username = Faker('user_name')
    password = Faker('password')

    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        kwargs['password'] = make_password(kwargs['password'])
        return super(UserFactory, cls)._create(model_class, *args, **kwargs)


@register
class ResumeFactory(DjangoModelFactory):
    title = Faker('text')
    status = 1
    phone = '+79833049235'
    email = Faker('email')
    user = SubFactory(UserFactory)

    class Meta:
        model = 'resume.Resume'
