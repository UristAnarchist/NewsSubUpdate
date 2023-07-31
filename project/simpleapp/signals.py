from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import truncatechars

from .models import News


@receiver(post_save, sender=News)
def product_created(instance, created, truncatechars=None, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новая статья в категории {instance.category}'

    text_content = (
        f'Статья: {instance.name}\n'
        f'Количество страниц: {instance.amount_of_pages}\n\n'
        f'{instance.price|truncatechars:20}'
        f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Статья: {instance.name}<br>'
        f'Количество страниц: {instance.price}<br><br>'
        f'{instance.price|truncatechars:20}'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на статью</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()