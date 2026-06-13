from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path(
        'register/',
        views.register
    ),

    path(
        'login/',
        views.login_user
    ),

    path(
        'logout/',
        views.logout_user
    ),
    path(
    'change-password/',
    views.change_password
    ),
    

    path(
    'password-reset/',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'
    ),
    name='password_reset'
),

path(
    'password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ),
    name='password_reset_done'
),

path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ),
    name='password_reset_confirm'
),

path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ),
    name='password_reset_complete'
),
]