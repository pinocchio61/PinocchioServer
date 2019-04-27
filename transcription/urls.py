# urls for transcription app

from django.urls import path

from . import views

app_name = 'transcription'

urlpatterns = [
    # ex: /transcription/
    path('', views.transcription, name='transcription'),
    # ex: /transcription/whee/
    path('whee/', views.whee, name='whee'),
]