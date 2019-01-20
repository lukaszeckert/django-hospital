from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class EmployForm(forms.ModelForm):
    class Meta:
        model = Employ
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'


class JobPositionForm(forms.ModelForm):
    class Meta:
        model = JobPosition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'


class EmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'


class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'

class CancelAppointment(forms.Form):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'


class FamilyDoctorForm(forms.ModelForm):
    class Meta:
        model = FamilyDoctor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'


class HospitalRooForm(forms.ModelForm):
    class Meta:
        model = HospitalRoom
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'


class ResidenceForm(forms.ModelForm):
    class Meta:
        model = Residence
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save.'))
        self.helper.template = 'hospital/form/base_from.html'
