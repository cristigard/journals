from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    
    path('register/', views.register, name = 'register'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('password_change/', views.UserChangePassView.as_view(), name = 'password_change'),
    path('password_change_done/', views.UserChangePassDoneView.as_view(), name = 'password_change_done'),

     path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]