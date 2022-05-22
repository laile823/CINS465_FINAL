import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Chef

@login_required
def api_add_chef(request):
    data = json.loads(request.body)
    body = data['body']
    
    chef = Chef.objects.create(body=body, created_by=request.user)
    
    return JsonResponse({'success': True})