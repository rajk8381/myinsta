

from django import forms
from .models import PublicUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    reapeat_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label="Full Name")
    class Meta:
        model =PublicUser
        fields =['first_name','email','password','reapeat_password']


    def clean_reapeat_password(self):
        password =self.cleaned_data.get('password')
        reapeat_password =self.cleaned_data.get('reapeat_password')
        if password!=reapeat_password:
            raise forms.ValidationError("Repeat Password Not Match.")
        elif len(password)<8:
            raise forms.ValidationError("Password must be 8 digit.")
        return reapeat_password

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if str(first_name).isnumeric():
            raise forms.ValidationError("Full Name Must be String.")
        return first_name

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "New Email Label"
        self.fields['email'].label = "New Email Label"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EditProfileForm(forms.ModelForm):
    dob=forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model =PublicUser
        fields =['image','first_name','about_me','mobile','gender','dob']


    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if str(first_name).isnumeric():
            raise forms.ValidationError("Full Name Must be String.")
        return first_name

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not str(mobile).isdigit():
            raise forms.ValidationError("Mobile Must be Number.")
        return mobile

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['mobile'].label = "Mobile"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    # email=forms.EmailField(widget=forms.TextInput(attrs={
    #     'class':'form-control',
    #     'type':'email',
    #     'placeholder':'Enter Email',
    # }))
    email=forms.EmailField()
    password=forms.CharField()
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = "Enter "+str(visible.name).title()



class ForgetPasswordForm(forms.Form):
    email=forms.EmailField()
    def __init__(self, *args, **kwargs):
        super(ForgetPasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = "Enter "+str(visible.name).title()


class ResetPasswordForm(forms.Form):
    new_password=forms.CharField()
    repeat_password = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = "Enter "+str(visible.name).title()

    def clean_repeat_password(self):
        new_password =self.cleaned_data.get('new_password')
        repeat_password =self.cleaned_data.get('repeat_password')
        if new_password!=repeat_password:
            raise forms.ValidationError("Repeat Password Not Match.")
        elif len(new_password)<8:
            raise forms.ValidationError("Password must be 8 digit.")
        return repeat_password