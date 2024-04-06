from django.urls import path
from . import views

handler404 = views.pageNotFound

urlpatterns = [
    path('login/', views.login_page, name='user_login'),
    path('register1/', views.register_page, name='user_register'),
    path("signup/", views.SignUp.as_view(), name="signup"),
]

