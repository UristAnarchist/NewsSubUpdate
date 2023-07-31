from django.urls import path
from .views import NewssList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, subscriptions

urlpatterns = [
   path('', NewssList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view()),
   path('search/', NewssList.as_view(template_name='search.html')),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('subscriptions/', subscriptions, name='subscriptions')
   ]