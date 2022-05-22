from django.apps import AppConfig
from django.http import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required

class feed(request):
    return render(request, 'feed/feed.html')

