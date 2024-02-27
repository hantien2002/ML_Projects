from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from accounts.forms import register_form

class RegisterView(CreateView):
    form_class = register_form.RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
