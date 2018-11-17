from django.urls import path
from . import views
from .views import create_news_letters
app_name = 'ballyapp'
urlpatterns = [
    #we are trying to assign a view called home_page to the root URL
    path('', views.home_page, name='home_page'),
    path('save/newsletter', views.create_news_letters, name='create_neskksdws_letter'),
    # path('', views.index, name='index'),
    # path('index.html', create_news_letters, name='index')
]