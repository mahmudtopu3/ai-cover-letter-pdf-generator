# forms.py
from django import forms

class CoverLetterForm(forms.Form):
    name = forms.CharField(label='Your Name')
    title = forms.CharField(label='Your Title', required=False)
    email = forms.EmailField(label='Your Email')
    phone = forms.CharField(label='Phone Number')
    linkedin = forms.CharField(label='LinkedIn Profile', required=False)
    year_of_experience = forms.IntegerField(label='Years of Experience', required=True)
    job_description = forms.CharField(widget=forms.Textarea, label='Job Description')


