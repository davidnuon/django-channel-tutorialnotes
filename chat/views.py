from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

class ChatWindow(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chat.html')