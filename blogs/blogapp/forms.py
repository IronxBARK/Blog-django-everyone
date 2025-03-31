from django import forms
from .models import BlogEntry

class EntryForm(forms.ModelForm):
    
    class Meta:
        model = BlogEntry
        fields = ['title', 'particular']
        widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
             'particular':forms.Textarea(attrs={'class':'form-control'}),
        }
        
        
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        particular = cleaned_data.get('particular')
        if len(title) < 3:
            raise forms.ValidationError("The title must be at least 3 characters long.")
        if len(particular) < 5:
            raise forms.ValidationError("The content must be at least 5 characters long.")
        return cleaned_data  # Ensure cleaned data is returned