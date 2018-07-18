from django.contrib.auth.models import User
from django import forms
from .models import  UserRatings, Movie

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','password']

class RateMovie(forms.Form):
    class Meta:
        model = UserRatings
        fields = ('user','movie','ratings')

    def save(self, commit=True):
        instance = super(RateMovie, self).save(commit=False)
        rating = self.cleaned_data['rating']
        movie = self.cleaned_data['movie']
        instance.save()
        return instance
