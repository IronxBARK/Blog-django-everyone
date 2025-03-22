#Mixins are used to give extra functionality to a class
#django's one mixin is LoginRequiredMixin which uses dispatch() and check if user is login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

class LoginRequired(LoginRequiredMixin):
    ''' Raise error if user is not authenticated or logged in '''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return PermissionDenied("You are not allowed to view this page")
        return super().dispatch(request, *args, **kwargs)