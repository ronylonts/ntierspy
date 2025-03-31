from django import forms
from .models import Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),
                Column('status', css_class='col-md-6'),
            ),
            'description',
            Row(
                Column('start_date', css_class='col-md-6'),
                Column('end_date', css_class='col-md-6'),
            ),
            Row(
                Column('budget', css_class='col-md-4'),
                Column('priority', css_class='col-md-4'),
                Column('client', css_class='col-md-4'),
            ),
            Submit('submit', 'Enregistrer', css_class='btn-primary')
        )