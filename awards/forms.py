from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from registration.forms import RegistrationForm

class RegisterForm(RegistrationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.helper.form_show_labels = True 