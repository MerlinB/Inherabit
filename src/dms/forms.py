from django import forms
from .models import Switch

        
class DMSForm(forms.ModelForm):
    timeframe = forms.IntegerField(help_text='Days without contact until activation.')
    secret = forms.CharField(help_text='Your Secret.', widget=forms.Textarea)
    beneficiary = forms.EmailField(help_text='Who gets the secret?')
    notification = forms.IntegerField(help_text='Days before activation when notification is send.')
    
    # Old solution:
    # def __init__(self, user, *args, **kwargs):
    #     super(DMSForm, self).__init__(*args, **kwargs)
    #     self.controller = user.controller
    
    class Meta:
        model = Switch
        fields = ['name', 'timeframe', 'notification', 'beneficiary', 'secret']
    
