from django.urls import path
from .views import HomeView, LoginView, ContactView, ProductView, AboutView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('contact', ContactView.as_view(), name='contact'),
    path('about', AboutView.as_view(), name='about'),
    path('register', RegisterView.as_view(), name='register'),
    path('product', ProductView.as_view(), name='product'),

]
