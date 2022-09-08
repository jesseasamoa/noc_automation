# imports necessary to build dashboard application
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import call_api
import json
# Create your views here.


class Login(TemplateView):
    """
    Login class to authenticate admin users
    """
    template_name = 'login.html'

    @method_decorator(csrf_protect)
    def post(self, request):
        if request.method == 'POST':
            uname = request.POST.get('uname')
            password = request.POST.get('password')
            user = authenticate(request, username=uname, password=password)
            if user is None:
                messages.error(request, 'Enter the right credentials!')
                return render(request, 'login.html')
            else:
                login(request, user)
                # messages.success(request, 'You are successfully loggedin!')
                return redirect('dashboard')

        return render(request, 'dashboard.html')


@csrf_protect
def logout_page(request):
    logout(request)
    messages.success(request, 'You are logged out. Login!')
    return redirect('login')


class Dashboard(LoginRequiredMixin, TemplateView):
    """
    Generating context data to render as dashboard consumable data
    """
    template_name = 'dashboard.html'

    api_data = call_api.api_call('reports/types', {})
    jsonResponse = json.loads(api_data.decode('utf-8'))
    # json_context = {'jsonResponse': jsonResponse}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headers'] = self.jsonResponse
        return context







