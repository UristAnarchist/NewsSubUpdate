from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
    )
    text = models.TextField()
    amount_of_pages = models.IntegerField(
        validators=[MinValueValidator(1)],
    )

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.name.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(
        User,
        blank=True,
        related_name='categories'
    )

    def __str__(self):
        return f'{self.name}'


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriber',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )

    def __str__(self):
        return f'пользователь {self.user} подписался на {self.category}'
