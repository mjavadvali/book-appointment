from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, UserType
from django import forms

class Userform(UserChangeForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = User
        fields = ["username", "email"]

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('type')
        is_staff = cleaned_data.get('is_staff')

        if user_type == UserType.patient.value and is_staff:
            raise forms.ValidationError("Patients cannot be staff members.")
        
        elif user_type == UserType.admin.value and not is_staff \
            or user_type == UserType.superuser.value and not is_staff:

            raise forms.ValidationError("Superusers and admins need to be staff members too.")



        return cleaned_data
    

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2
    
        
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user
    


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields