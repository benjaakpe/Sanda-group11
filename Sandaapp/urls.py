from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'Sandaapp'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='Sandaapp/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='Sandaapp/logout.html'), name="logout"),
    re_path(r'^password_reset/$', auth_view.PasswordResetView.as_view(
        template_name="Sandaapp/password_reset_form.html"),
            name='password_reset'),
    re_path(r'^password_reset/done/$', auth_view.PasswordResetDoneView.as_view(
        template_name="Sandaapp/password_reset_done.html"),
            name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_view.PasswordResetConfirmView.as_view(
                template_name="Sandaapp/password_reset_confirm.html"),
            name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_view.PasswordResetCompleteView.as_view(
            template_name= "../Sandaapp/password_reset_complete.html"),
            name='password_reset_complete'),
]
