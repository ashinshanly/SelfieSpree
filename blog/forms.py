#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.files.images import get_image_dimensions
#from .models import Profile, SignUp

# If you don't do this you cannot use Bootstrap CSS
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		#docstring fos Meta
		model = User
		fields = (
			'username',
			
			'email',
			'password1',
			'password2'
			)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.username = self.cleaned_data['username']
		#user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user 
	



class EditProfileForm(UserChangeForm):

	class Meta:

		model= User

		fields=(

			'first_name', 'last_name', 'email'
						
			) 





"""class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')




	


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pic', 'user', 'college', 'city', 'bio')






class ContactForm(forms.Form):
    full_name=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields= ['full_name','email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
    def clean_full_name(self):
        full_name=self.cleaned_data.get('full_name')
        return full_name   """
		



    	

    	


	

	

	

	




		

	

	