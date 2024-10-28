from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
class register(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')

class LogoutView(View):
    template_name = 'registration/logout_confirmation.html'

    def post(self, request, *args, **kwargs):
        logout(request)  # Log out the user
        return redirect('home')  # Redirect to the home page after logging out

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  # Render the logout confirmation page
