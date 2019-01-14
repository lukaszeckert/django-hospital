from django import forms
from .models import HospitalStaff, JobPosition, Employment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class EmployForm(forms.ModelForm):
    class Meta:
        model = HospitalStaff
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save employ'))
        self.helper.template = 'polls/form/base_from.html'


class JobForm(forms.ModelForm):
    class Meta:
        model = JobPosition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save job.'))
        self.helper.template = 'polls/form/base_from.html'


class EmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save employment.'))
        self.helper.template = 'polls/form/base_from.html'

