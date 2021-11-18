from django.urls import path
from . import views
from login.views import accountView

app_name = 'real'

urlpatterns = [
    path('', accountView.Login, name='login'),
    path('signup/', accountView.SignUpView.as_view(), name='signup'),
    path('top/', views.Top, name='base'),
    path('password_reset/', accountView.PasswordChange.as_view(), name='password_reset'),
]
