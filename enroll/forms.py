from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User

class TaskInfo(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed', 'desc']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter tasks here'}),
            'completed':forms.CheckboxInput(),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
        }
        labels ={'title': 'Title', 'desc': 'Description'}

class LoginForm(AuthenticationForm):   
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder': 'Enter Username'}), label_suffix='') 
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'currentpassword', 'class':'form-control', 'placeholder': 'Enter Password'}), label_suffix='') 

class SignupForm(UserCreationForm):

    # Below fields are used only for label sufffix, widget
    username = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label_suffix='', widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label_suffix='', widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label_suffix='', widget= forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',label_suffix='', widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    password2 = forms.CharField(label='Confirm Password', label_suffix='', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels ={
            'first_name': 'First Name','last_name': 'Last Name', 'email': 'Email'
        }

class EditUserProfile(UserChangeForm):
    password = None
    username = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label_suffix='', widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label_suffix='', widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label_suffix='', widget= forms.TextInput(attrs={'class':'form-control'}))
    date_joined = forms.CharField(label_suffix='', widget= forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(label_suffix='', widget= forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {
            'email':'Email'
        }

class PCForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',label_suffix='', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password',label_suffix='', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')
        
