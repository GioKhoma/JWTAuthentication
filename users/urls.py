from django.urls import path
from .views import Home, LoginView, RegisterView, LogoutView

urlpatterns = [
    path('home/', Home.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]