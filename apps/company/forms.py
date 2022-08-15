from django import forms
from .models import Contact


class ApplyModelForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = (
			 "full_name",
			 "own_phone",
			 "extra_phone",
			 "message",
			 "category"
			)