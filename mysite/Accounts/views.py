from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import  reverse_lazy
from django.shortcuts import  render
from django.contrib.auth.decorators import login_required

from . import forms

# Create your views here.
class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("URLShortener:user_home" )
    template_name = "Accounts/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        return form_class(self.request, **self.get_form_kwargs() )

    def form_valid(self, form):
        login(self.request, form.get_user() )
        return super(LoginView, self).form_valid(form)

@login_required(login_url='/')
def LogoutView(request):
    logout(request)
    return render(request, "index.html", {'is_logout': True})
'''
class LogoutView(generic.RedirectView):
    #url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('home', *args, kwargs={'is_logout': False})'''

class CreateUserView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "Accounts/create_user.html"

@login_required(login_url='/')
class EditUserView(generic.UpdateView):
    model = User

    def get_queryset(self):
        return self.model.objects.filter(username=str(self.request.user.username))