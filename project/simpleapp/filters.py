from django_filters import FilterSet

from .models import News

class NewsFilter(FilterSet):

   class Meta:
       model = News
       fields = {
           'name': ['icontains'],
           'text': ['icontains'],
           'category': ['exact'],
           'amount_of_pages': [
           'lt',
           'gt',],
           'date': ['date__gt'],
       }