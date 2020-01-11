from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your First Name'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Last Name'
            }
        )
    )
    username = forms.CharField(
        label="Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your User Name'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your password'
            }
        )

    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile Number'
            }
        )

    )
    email = forms.EmailField(
        label="Enter Your EmailID",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your email id'
            }
        )
    )

    GENDER_CHOICE = (
        ('Male','MALE'),
        ('Female','FEMALE')

    )

    gender = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=GENDER_CHOICE,
        label="Select Your Gender"
    )

    y = range(1960,2020)
    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=y),
        label="Enter Your Date_Of_Birth"
    )




class LoginForm(forms.Form):
    user_name = forms.CharField(
        label="Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your User Name'
            }
        )
    )
    password= forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Password'
            }
        )
    )