from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Reader


class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=500)
    phone = forms.CharField(max_length=15)
    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'address',
            'phone',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        reader = Reader()

        if commit:
            user.save()
            reader.user = user
            reader.name = self.cleaned_data['name']
            reader.address = self.cleaned_data['address']
            reader.phone = self.cleaned_data['phone']
            reader.readerType = 'reader'
            reader.save()

        return user, reader
