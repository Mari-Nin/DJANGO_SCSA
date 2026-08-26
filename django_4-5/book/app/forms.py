from django import forms
from .models import Book, Readership

class BookForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label="Book title",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter book name'
        })
    )
    
    language = forms.CharField(
        max_length=20,
        label='Language of book',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter language of book'
        })
    )

    type = forms.CharField(
        max_length=20,
        label='Type of book',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter type of book'
        })
    )
    
    comment = forms.CharField(
        max_length=100,
        label='Comment on this book',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter comment'
        })
    )

from django import forms
from .models import Readership

class ReaderModelship(forms.ModelForm):
    class Meta:
        model = Readership
        fields = '__all__' 
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address'
            }),
       
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter comment'
            })
        }
    def clean_email(self):
            email = self.cleaned_data['email']
            if not email.endswith('@gmail.com'):
                raise forms.ValidationError('Email must be from @gmail.com')
            return email