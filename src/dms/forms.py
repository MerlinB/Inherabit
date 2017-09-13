from django import forms
from .models import Switch,  Controller

        
class DMSForm(forms.ModelForm):
    timeframe = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Days without contact until activation.','min':1})) #help_text='Days without contact until activation.')
    secret = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Secret.'})) #help_text='Your Secret.', widget=forms.Textarea)
    beneficiary = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Who gets the secret?'})) #help_text='Who gets the secret?')
    notification = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Days before activation when notification is send.','min':1})) #help_text='Days before activation when notification is send.')
    
    # Old solution:
    # def __init__(self, user, *args, **kwargs):
    #     super(DMSForm, self).__init__(*args, **kwargs)
    #     self.controller = user.controller
    
    class Meta:
        model = Switch
        fields = ['name', 'timeframe', 'notification', 'beneficiary', 'secret']
