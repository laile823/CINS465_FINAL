from django.http import QueryDict
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Chef

@login_required
def feed(request):
    userids = [request.user.id]

    for chefer in request.user.chefwikiprofile.follows.all():
        userids.append(chefer.user.id)

    chefs = Chef.objects.filter(created_by_id__in=userids)

    return render(request, 'feed/feed.html', {'chefs': chefs})
# Create your views here.

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        chefers = User.objects.filter(username__icontains=query)
    else:
        chefers = []
    
    context = {
        'query': query,
        'chefers':  chefers
    }

    return render(request, 'feed/search.html', context)