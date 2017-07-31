from django import forms
from .models import Switch

        
class DMSForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        super(DMSForm, self).__init__(*args, **kwargs)
        self.controller = user.controller
    
    class Meta:
        model = Switch
        fields = ['timeframe']
    
