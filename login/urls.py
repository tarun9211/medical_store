from django.urls import path, include
import views

urlpatterns = [
    path('signup/', views.signup_form_view, name='signup-url'),
    path('signin/', views.sign_in_view, name='signin-url'),
]