from django import forms
from .models import Profile
# Create your forms here.

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'max_temp', 'min_temp', 'max_hum', 'min_hum', 'fan_int', 'fan_dur','applied']