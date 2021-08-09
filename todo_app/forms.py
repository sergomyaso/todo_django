from django import forms
from django.contrib.auth.models import User


class NoteForm(forms.Form):
    title = forms.CharField(label="Title", max_length=128)
    text = forms.CharField(label="Your Note:", max_length=128)
