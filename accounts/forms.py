

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
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

