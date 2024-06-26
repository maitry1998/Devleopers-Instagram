from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from .models import Skill, Message
class CustomUser(UserCreationForm):
    class Meta:
        model= User
        fields=['first_name','email','username','password1','password2']
        labels={
            'first_name':"Name"
        }

    def __init__(self, *args, **kwargs):
        super(CustomUser, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        # fields= '__all__'
        exclude = {'user'}
        labels={
            'first_name':"Name"
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class SkillForm(ModelForm):
    class Meta:
        model= Skill
        # fields= '__all__'
        fields="__all__"
        exclude=["owner"]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']
        
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        


