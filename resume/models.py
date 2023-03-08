from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Resume(models.Model):
    class Status(models.IntegerChoices):
        looking = 1, 'В активном поиске'
        open_to_suggestions = 2, 'Открыт к предложениям'
        not_looking = 3, 'Не ищу работу'

    user = models.ForeignKey(User, related_name='resume', on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=Status.choices, default=Status.looking, verbose_name=_('Статус'))
    grade = models.SmallIntegerField(verbose_name=_('Рейтинг'), null=True, blank=True)
    specialty = models.CharField(max_length=1024, verbose_name=_('Специальность'), null=True, blank=True)
    salary = models.IntegerField(verbose_name=_('Зароботная плата'), null=True, blank=True)
    education = models.CharField(max_length=1024, verbose_name=_('Образование'), null=True, blank=True)
    experience = models.CharField(max_length=1024, verbose_name=_('Опыт'), null=True, blank=True)
    portfolio = models.TextField(verbose_name=_('Портфолио'), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name=_('Название'))
    phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name=_('Телефон для связи'))
    email = models.EmailField(unique=True, verbose_name=_('Электронная почта'))
