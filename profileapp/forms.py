from django import forms
from .models import Profile,Profileskills


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname','lastname','email','profilepic','phoneno','address']
        labels = {
            'firstname':'First Name',
            'lastname':'Last Name',
            'email':'Email',
            'phoneno':'Phone No',
            'address':'Address',
            'profilepic':'Profile Pic'

        }
        widgets = {
            'firstname': forms.TextInput(attrs={'class':'form-control','id':'firstname','placeholder': 'Enter First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter email'}),
            'phoneno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone No'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address'})
        }
    # def __init__(self,*args, **kwarg):
    #     super().__init__(*args, **kwarg)
    #     if self.instance and self.instance.profilepic:
    #         self.fields.pop('profilepic')





    def clean(self):
        super(ProfileForm,self).clean()

        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        email = self.cleaned_data.get('email')



        if len(firstname) < 3:
            self._errors['firstname'] = self.error_class(['First Name Minimum 3 characters required'])
        elif len(lastname) < 3:
            self._errors['lastname'] = self.error_class(['Last Name Minimum 3 characters required'])
        elif not forms.EmailField().clean(email):
            self._errors['lastname'] = self.error_class(['Enter a valid email address'])
        return self.cleaned_data
