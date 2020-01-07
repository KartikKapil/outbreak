from django.urls import path
from django.contrib.auth import views as djViews
from . import views

urlpatterns = [
    path('login/', djViews.LoginView.as_view(
        template_name='home.html'), name='login'),
    path('signup/patient/', views.signup_p, name='signup_p'),
    path('signup/hospital/', views.signup_h, name='signup_h'),
    path('dashboard/', views.dashboard, name='dashboard')
]
