from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views import View

from .forms import RegisterFrom

class LoginView(View):
    template_name = "users/login.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "username_value": "",
                "errors": {},
                "non_field_errors": []
            }
        )
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    
                }
            )