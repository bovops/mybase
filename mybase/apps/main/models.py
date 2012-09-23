# -*- coding: utf8 -*-

from django.db import models
from forms import *
# Create your models here.
STATUS_CHOICES = (
    (0, 'Свободен'),
    (1, 'Приостановлен'),
    (2, 'Активен')
)

class Client(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Наименование')
    descr = models.TextField(max_length=10000, blank=True, verbose_name='Описание')
    status = models.SmallIntegerField(max_length=1, choices=STATUS_CHOICES, default=2)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'{0}' .format(self.name)
