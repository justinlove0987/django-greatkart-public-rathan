from django import forms
from django.forms import fields
from .models import Account, UserProfile


class RegistreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter Password",
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm Password"
    }))

    class Meta:
        model = Account
        fields = ["first_name", "last_name",
                  "phone_number", "email", "password"]

    def __init__(self, *args, **kwargs):
        super(RegistreationForm, self).__init__(*args, **kwargs)

        # this also works!
        # placeholder = ["Enter First Name", "Enter Last Name",
        #                "Enter Phone Number", "Enter Email",
        #                "Enter Password", "Confirm Password"]

        # for field_index, field in enumerate(self.fields):
        #     self.fields[field].widget.attrs["placeholder"] = placeholder[field_index]

        self.fields["first_name"].widget.attrs["placeholder"] = "Enter First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Enter Last Name"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Enter Phone Number"
        self.fields["email"].widget.attrs["placeholder"] = "Enter Email"

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    def clean(self):
        cleaned_data = super(RegistreationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match."
            )


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number',)
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"



class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, 
    error_messages= {"invalid":("Images files only")}, widget=forms.FileInput)


    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture',)
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
