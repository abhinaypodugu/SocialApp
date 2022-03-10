from email.policy import default
from django import forms

class textForms(forms.Form):
    
    text = forms.CharField(max_length=100, required=False,
            widget=forms.TextInput( attrs=
            {'class': 'form-control', 'placeholder' : 'Enter Text Here', 'aria-describedby': 'add-btn'}
            )
            )

class ImageForm(forms.Form):

    image = forms.ImageField(widget=forms.FileInput())
    imgText = forms.CharField(max_length=100, required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Text Here', 'aria-describedby': 'add-btn'}
                                                  )
                           )
