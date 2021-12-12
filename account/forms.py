from django.forms import ModelForm,Textarea,CharField,TextInput,EmailInput,Select,PasswordInput
from django.contrib.auth.models import User
from .models import Accounts,Department
# department_choices = (('publicity','Publicity'),('security','Security'),('entertainment','Entertainment'),('secretary','Secretary'),('volunteer','Volunteer'),('journalist','Journalist'))

class AccountsForm(ModelForm):
    
    class Meta:
        model = Accounts
        fields = ['user','name', 'department', 'position','uni','phone_number','email']
        labels ={
            "uni":"University",
        }
        widgets = {
            'user':Select(choices=User.objects.all(),attrs={'class':'form-control',}),
            'name':TextInput(attrs={'class':'form-control',}),
            # 'department':TextInput(attrs={'class':'form-control',}),
            'department':Select(choices=Department.objects.all(),attrs={'class':'form-control',}),
            'position':TextInput(attrs={'class':'form-control',}),
            'uni':TextInput(attrs={'class':'form-control'}),
            'phone_number':TextInput(attrs={'class':'form-control',}),
            'email':EmailInput(attrs={'class':'form-control',}),
        }


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput(attrs={'class': 'input form-control'}))
    password2 = CharField(label="Repeat password", widget=PasswordInput(attrs={'class ': 'input form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'input form-control ', 'autofocus': True}),
            'email': EmailInput(attrs={'class': 'input form-control', 'required': True})
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password2']

