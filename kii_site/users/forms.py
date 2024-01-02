from django import forms
from .models import Account


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {'username': forms.TextInput({'class': 'textinput form-control newinput',
                                          'placeholder': 'username',
                                          'id':'inputformcolor'}),
                   'email': forms.EmailInput({'class': 'textinput form-control',
                                        'placeholder': 'email'}),
                   'first_name': forms.TextInput({'class': 'textinput form-control',
                                            'placeholder': 'First name'}),
                   'last_name': forms.TextInput({'class': 'textinput form-control',
                                           'placeholder': 'Last name'}),
                   }

from .models import Account
class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['department', 'vk','instagram','telegram', 'account_image']
        widgets = {'department': forms.TextInput({'class': 'textinput form-control',
                                       'placeholder': 'department'}),
                   'vk': forms.TextInput({'class': 'textinput form-control',
                                      'placeholder': 'vk'}),
                   'instagram': forms.TextInput({'class': 'textinput form-control',
                                         'placeholder': 'instagram'}),
                   'telegram': forms.TextInput({'class': 'textinput form-control',
                                           'placeholder': 'telegram'}),
                   'account_image': forms.FileInput({'class': 'form-control',
                                       'placeholder': 'image'})
                   }