from django import forms
from appTwo.models import MyUser

class NewUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'


    