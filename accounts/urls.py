from django.urls import path
from .views import login_page, register_page, activate_email_account

urlpatterns = [
    path('login/', login_page, name='login',),
    path('register/', register_page, name='register',),
    path('activate/<email_token>/', activate_email_account, name='activate_email',),
]
