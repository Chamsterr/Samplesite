from django.forms import ModelForm
from .models import Bb


class BbForm(ModelForm):
    class Meta:
        models = Bb
        fields = ('title', 'content', 'price', 'rubric')