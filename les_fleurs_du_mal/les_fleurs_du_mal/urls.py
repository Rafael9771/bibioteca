
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(r'password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html",), name='password_reset'),
    path(r'password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path(r'reset/(<uidb64>)/(<token>)/',
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path(r'reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^biblioteca/', include('aplications.biblioteca.urls')),

]
