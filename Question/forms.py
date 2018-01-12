from django import forms

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db.models import Q

# from .models import USERNAME_REGEX

from .models import Question
from .utils import code_generator


class QuestionCreateormForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    title        = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the product'}))
    description  = forms.CharField(widget=forms.Textarea(attrs={'required': True,'class': 'form-control','placeholder': 'Description of the product'}))
    terms_and_condition = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Terms and condition'}))

    division   = forms.ChoiceField(required=True, choices=[(x, x) for x in range(1,8)], widget=forms.Select(attrs={'class': 'form-control'}))
    city       = forms.ChoiceField(required=True, choices=[(x, x) for x in range(1, 8)], widget=forms.Select(attrs={'class': 'form-control'}))
    thana      = forms.ChoiceField(required=True, choices=[(x, x) for x in range(1,8)], widget=forms.Select(attrs={'class': 'form-control'}))

    price = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Rent price of the product'}))

    rental_period = forms.ChoiceField(required=True, choices=[(x, x) for x in range(1, 4)],
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(required=True, choices=[(x, x) for x in range(1, 4)],
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    brand = forms.ChoiceField(required=True, choices=[(x, x) for x in range(1, 4)],
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    discount = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Discount'}))

    first_image = forms.ImageField(required=True)

    class Meta:
        model = Question
        exclude = ('user', 'rentedBy', 'slug','is_available','has_discount')
        # fields = ('username', 'email',)
        # fields = ('first_name', 'last_name', 'division', 'city', 'thana', 'national_id', 'passport_number')

    def save(self, commit=True):
        # Save the provided password in hashed format
        print("in save!")
        question = super(QuestionCreateormForm, self).save(commit=False)

        if commit:
            question.save()
        return question
