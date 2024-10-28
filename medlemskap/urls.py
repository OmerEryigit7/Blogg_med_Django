from django.urls import path
from .views import register
from .views import LogoutView

urlpatterns = [
    path('lag_bruker/', register.as_view(), name='sign_up'),
    path('logg_ut/', LogoutView.as_view(), name='logout_confirmation')
]