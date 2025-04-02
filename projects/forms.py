from django import forms
from .models import Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.validators import MinValueValidator
from django.utils import timezone

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        
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
            'budget',
            Submit('submit', 'Enregistrer', css_class='btn-primary float-end')
        )
        
        # Ajout de classes CSS aux champs
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-select'})
        self.fields['budget'].widget.attrs.update({'class': 'form-control'})
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        budget = cleaned_data.get('budget')
        
        # Validation des dates
        if start_date and end_date:
            if start_date > end_date:
                self.add_error('end_date', "La date de fin doit être postérieure à la date de début")
            
            if start_date < timezone.now().date():
                self.add_error('start_date', "La date de début ne peut pas être dans le passé")
        
        # Validation du budget
        if budget is not None and budget < 0:
            self.add_error('budget', "Le budget ne peut pas être négatif")
        
        return cleaned_data