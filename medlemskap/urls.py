from django.urls import path
from .views import register

urlpatterns = [
    path('lag_bruker/', register.as_view(), name='sign_up')
]