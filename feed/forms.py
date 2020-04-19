from accounts.models import Bio
from django import forms


class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ('fullname', 'displayimage','status','email')
