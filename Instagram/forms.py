from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class  NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes','comments']



class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    def save(self,commit=True):
        user=super().save(commit=false)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
            return user
