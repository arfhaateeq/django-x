from django.contrib.auth.models import User
from django import forms

class EditProfileForm(forms.ModelForm):
    password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput,
        required=False
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        # Only validate if a new password was entered
        if p1 or p2:
            if p1 != p2:
                raise forms.ValidationError("Passwords do not match.")

        return cleaned_data