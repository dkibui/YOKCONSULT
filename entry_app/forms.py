from django import forms


def should_be_empty(value):
    if value:
        raise forms.ValidationError("Field is not empty")


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=80,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"}),
    )
    phone = forms.CharField(
        max_length=13,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter your phone number"}),
    )
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter your email"}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Tell us something..."}),
        required=True,
    )
    forcefield = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave empty",
        validators=[should_be_empty],
    )
