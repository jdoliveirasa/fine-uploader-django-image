from django import forms

class UploadFileForm(forms.Form):
	csrfmiddlewaretoken = forms.CharField(max_length=255)
	qquuid = forms.CharField(max_length=255)
	qqfilename = forms.CharField(max_length=255)
	qqtotalfilesize = forms.CharField(max_length=255)
	qqfile = forms.FileField()