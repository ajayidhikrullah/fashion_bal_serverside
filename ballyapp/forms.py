from django import forms
from .models import news_letters

class CreateSignUpLetterForm(forms.ModelForm):
    class Meta:
        model = news_letters
        fields = ['email']
    #     model = news_letters
    # user_mails = forms.EmailField(max_length=100)
    email = forms.EmailField (max_length=100)
