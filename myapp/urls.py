from django.urls import path
from django.contrib.auth import views as auth_views
from .views import authentication_page, pages, user_management


urlpatterns = [
     path('', pages.home, name='home'),
     path('about/', pages.about, name='about'),
     path('signup/', authentication_page.signupPage, name='signup'),
     path('login/', authentication_page.loginPage, name='login'),
     path('logout/', authentication_page.logoutUser, name='logout'),
     path('activate-user/<uidb64>/<token>', authentication_page.activate_user, name='activate'),
     path('update_user/<str:pk>/', user_management.updateUser, name='update-user'),
     
     path(
        'reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), 
        name='password_reset'
    ),
    path(
        'reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), 
        name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), 
        name='password_reset_confirm'),
    path(
        'reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), 
        name='password_reset_complete'),
]