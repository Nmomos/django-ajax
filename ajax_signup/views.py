from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_used': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_used']:
        data['error_message'] = 'このユーザー名は既に使用されています'
    return JsonResponse(data)