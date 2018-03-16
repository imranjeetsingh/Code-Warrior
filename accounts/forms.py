from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password', 'is_active', 'score', 'admin')

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Password'}
    ))

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        response = {
            'success': False,
            'message': 'Login failed.'
        }

        user = authenticate(request, username=username, password=password)
        # If the is_active field is false, then the authenticate() method by default returns None
        if user is None:
            response['message'] = 'The username or the password is incorrect! Please try again.'
            # raise forms.ValidationError('Invalid credentials')
            return response
        login(request, user)
        response['success'] = True
        self.user = user
        return response



class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Username'}
    ))
    full_name = forms.CharField(label='Full Name', widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Full Name'}
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Email'}
    ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Password'}
    ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Password'}
    ))

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True  # TODO: set it to False and enable email activation
        if commit:
            user.save()
        return user
