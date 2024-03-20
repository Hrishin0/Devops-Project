from django import forms
from django.forms import ModelForm
from .models import Sign

#create form here

class PetForm(ModelForm):
    class Meta:
        model = Sign
        fields = ('name','breed', 'age', 'description', 'image')
        labels = {
                'name': '',
                'breed':'',
                'age':'',
                'description':'',
                'image':'',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'breed':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Breed'}),
            'age':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Age'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
        }
        