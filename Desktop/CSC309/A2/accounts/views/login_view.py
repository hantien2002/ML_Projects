from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from accounts.forms import login_form

class LoginView(FormView):
    form_class = login_form.LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:profile_edit')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return render(self.request,
                          self.template_name,
                          context={'form': form,
                                   'error_message': 'Invalid username or password'})
        return super().form_valid(form)