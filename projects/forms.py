from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import Project, Review
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image','description','demo_link','source_link','tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    # This method is very nimportnat to give styling of css to the input IF YOU ARE USING MODEL FORM
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



  
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add your comment'
        }


    # This method is very nimportnat to give styling of css to the input
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            field.widget.attrs.update({'style': 'width: 100% !important;padding: 1rem;  border-radius: 8px;'})
      