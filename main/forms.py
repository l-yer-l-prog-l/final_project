from django import forms
from .models import Answer, Profile, RatingTeacher
from django.contrib.auth.models import User


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['title', 'description']

        widjets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TeacherRatingForm(forms.ModelForm):

    class Meta:
        model = RatingTeacher
        fields = ('rating',)
