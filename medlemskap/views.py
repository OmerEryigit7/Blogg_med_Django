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

    def post(self, request):
        logout(request)
        return redirect('home')

    def get(self, request):
        return render(request, self.template_name)
