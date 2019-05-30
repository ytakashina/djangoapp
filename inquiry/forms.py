from django import forms
from inquiry.models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('user_name', 'email', 'sex', 'job', 'inquiry_text')
        widgets = {
            'user_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'sex': forms.RadioSelect(),
            'job': forms.Select(attrs={"class": "form-control"}),
            'inquiry_text': forms.Textarea(attrs={"class": "form-control", "cols": "10", "rows": "4"}),
        }
