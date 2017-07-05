from django import forms

class LoginPage(forms.Form):
	username = forms.CharField(label='username', max_length=32, required=True, error_messages={'required': 'Please enter your Username'})
	password = forms.CharField(label='password', max_length=32, required=True, error_messages={'required': 'Please enter your Password'})
	#remember_me = forms.BooleanField(label='Rememberme',required=False)

class ForgetPage(forms.Form):
	forget_email = forms.EmailField(label='forget_email', max_length=64, required=True, error_messages={'required': 'Please enter your email'})
	forget_username = forms.CharField(label='forget_username', max_length=64, required=True, error_messages={'required': 'Please enter your username'})

class ForgotPage(forms.Form):
	forgot_email = forms.EmailField(label='forgot_email', max_length=64, required=True, error_messages={'required': 'Please enter your email'})
	
class RegisterPage(forms.Form):
	reg_email = forms.EmailField(label='reg_email', max_length=32, required=True, error_messages={'required': 'Please enter your Email'})
	reg_username = forms.CharField(label='reg_username', max_length=32, required=True, error_messages={'required': 'Please enter your Username'})
	reg_password = forms.CharField(label='reg_password', max_length=32, required=True, error_messages={'required': 'Please enter your Password'})
	
class ChangePasswordPage(forms.Form):
	change_currentPassword = forms.CharField(label='change_currentPassword', max_length=32, required=True, error_messages={'required': 'Please enter your Username'})
	change_newPassword = forms.CharField(label='change_newPassword', max_length=32, required=True, error_messages={'required': 'Please enter your Password'})
	change_nnewPassword = forms.CharField(label='change_nnewPassword', max_length=32, required=True, error_messages={'required': 'Please enter your Email'})