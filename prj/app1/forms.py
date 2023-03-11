from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app1.models import Item


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'item_img', 'slug', 'owner']

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.owner = self.cleaned_data['owner']
    #     instance.url = slugify(self.cleaned_data['name'])
    #     if commit:
    #         instance.save()
    #     return instance


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form_input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    email = forms.CharField(label='email', widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'email', 'password2']
