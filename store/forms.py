from django import forms
from .models import Product,ReviewRating
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject','review','rating']