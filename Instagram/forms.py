from django import forms



class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    def save(self,commit=true):
        user=super().save(commit=false)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
            return user
            