from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from accounts.forms import profile_edit_form

class ProfileEditView(FormView):
    form_class = profile_edit_form.ProfileEditForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile_view')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorized', status=401)

    def get_initial(self):
        inital = super().get_initial()
        inital['email'] = self.request.user.email
        inital['first_name'] = self.request.user.first_name
        inital['last_name'] = self.request.user.last_name
        return inital.copy()

    def form_valid(self, form, **kwargs):
        user = self.request.user
        if 'password1' in form.cleaned_data and form.cleaned_data['password1'] != '':
            if ('password2' not in form.cleaned_data) and form.cleaned_data['password1'] != form.cleaned_data['password2']:
                context = self.get_context_data(**kwargs)
                context['error_message'] = 'Passwords do not match'
                return self.render_to_response(context)
            else:
                if len(form.cleaned_data['password1']) < 8:
                    context = self.get_context_data(**kwargs)
                    context['error_message'] = 'Password must be at least 8 characters long'
                    return self.render_to_response(context)
                else:
                    user.set_password(form.cleaned_data['password1'])

        if 'email' in form.cleaned_data:
            if '@' in form.cleaned_data['email'] or form.cleaned_data['email'] == "":
                user.email = form.cleaned_data['email']
            else:
                context['error_message'] = 'Invalid email'
                return self.render_to_response(context) 

        if 'first_name' in form.cleaned_data:
            user.first_name = form.cleaned_data['first_name']

        if 'last_name' in form.cleaned_data:
            user.last_name = form.cleaned_data['last_name']

        user.save()
        update_session_auth_hash(self.request, user)
        return super().form_valid(form)
