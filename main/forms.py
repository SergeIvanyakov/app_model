from .models import Article
from django.forms import ModelForm
from django import forms

class ArticleForm(forms.Form):
    name = forms.CharField(max_length=250)
    age = forms.FloatField()
    gender = forms.FloatField()
    height = forms.FloatField()
    weight = forms.FloatField()
    ap_hi = forms.FloatField()
    ap_lo = forms.FloatField()
    cholesterol = forms.FloatField()
    gluc = forms.FloatField()
    smoke = forms.FloatField()
    alco = forms.FloatField()
    active = forms.FloatField()
    cardio = forms.FloatField()
    bp_category = forms.FloatField()