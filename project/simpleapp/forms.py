from django import forms
from django.core.exceptions import ValidationError
from .models import News

class NewsForm(forms.ModelForm):
   class Meta:
       model = News
       fields = [
           'name',
           'text',
           'category',
           'amount_of_pages',
           'date'
       ]

   def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("text")
       if text is not None and len(text) < 20:
           raise ValidationError({
               "text": "Текст не может быть менее 20 символов."
           })
       name = cleaned_data.get("name")
       if name == text:
           raise ValidationError(
               "Текст статьи не должен быть идентичен названию."
           )

       return cleaned_data