from django.views.generic import TemplateView, CreateView
from .models import Users
from .forms import SignupForm


class RegisterView(CreateView):
    model = Users
    success_url = '/'
    form_class = SignupForm
    template_name = 'register.html'


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ProductView(TemplateView):
    template_name = 'product.html'


class LoginView(TemplateView):
    template_name = 'login.html'
