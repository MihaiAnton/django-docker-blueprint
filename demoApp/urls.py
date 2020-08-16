from django.urls import path

from .views import index, json, html

app_name = 'demoApp'

urlpatterns = [
    path('', index, name='index'),
    path('json/', json, name='json'),
    path('html/', html, name='html')
]
