from django import forms

from .models import ChefWikiProfile

class CheferProfileForm(forms.ModelForm): 
    class Meta:
        model = ChefWikiProfile
        fields =('avatar',)
