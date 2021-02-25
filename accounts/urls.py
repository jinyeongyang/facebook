from django.urls import path

from accounts.views import signup, login_check

app_name = 'accounts'

urlpatterns =[
    path('signup/', signup, name='signup'),
    path('login/', login_check, name='login'),
]