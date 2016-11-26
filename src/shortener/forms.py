from django import forms

from .validators import validate_url, validate_dot_com


class SubmitUrlForm(forms.Form):
	url=forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])


	

	# def clean(self):
	# 	cleaned_data= super(SubmitUrlForm, self).clean()
	# 	url=cleaned_data.get('url')

	# 	url_validator = URL_Validator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("invalid URL for this Field")
	# 	return url
	
	# def clean_url(self):
	# 	url=self.cleaned_data['url']
	# 	if not "com" in url:
	# 		raise forms.ValidationError("This is not valid because of no .com")

	# 	#print(url)
	# 	# url_validator = URL_Validator()
	# 	# try:
	# 	# 	url_validator(url)
	# 	# except:
	# 	# 	raise forms.ValidationError("invalid URL for this Field")
	# 	return url
