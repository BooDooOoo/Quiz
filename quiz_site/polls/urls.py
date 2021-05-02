from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('test/', test, name='test'),
    path('api/get_poll_questions/<int:pk>/', get_questions, name='get_poll_questions'),
    path('api/save_user_choices/', user_choices, name='save_user_choices'),
    path('api/completed_polls/', completed_polls),
    path('completed_polls/', completed_polls_view, name='completed_polls')
]