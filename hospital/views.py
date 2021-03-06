from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, CreateView
from django.forms import formset_factory
from .filters import *
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    return redirect("employ")

def employ_list_view(request):
    obj = Employ.objects.annotate(salary=Func(F('id'), function='salary')).all()
    filter = EmployFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/employ.html', {'filter': filter})


class EmployCreateView(CreateView):
    model = Employ
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class EmployUpdateView(UpdateView):
    model = Employ
    form_class = EmployForm
    template_name = 'hospital/update_view/employ_update_view.html'


class EmployDeleteView(DeleteView):
    model = Employ

    def get_object(self, queryset=None):
        obj = super(EmployDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/employ')

def employ_raise_view(request):
    try:
        if float(request.POST['percent']) <= 0:
            messages.error(request, "Percent must be greater than 0")
            return HttpResponseRedirect('/hospital/employ')
    except:
        messages.error(request, "Enter a number")
        return HttpResponseRedirect('/hospital/employ')

    with connection.cursor() as cursor:
        cursor.execute("SELECT raise_salary(%s)", [request.POST['percent']])
    
    return HttpResponseRedirect('/hospital/employ')

def jobposition_list_view(request):
    obj = JobPosition.objects.all()
    filter = JobPositionFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/jobposition.html', {'filter': filter})


class JobPositionCreateView(CreateView):
    model = JobPosition
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class JobPositionUpdateView(UpdateView):
    model = JobPosition
    form_class = JobPositionForm
    template_name = 'hospital/update_view/employ_update_view.html'


class JobPositionDeleteView(DeleteView):
    model = JobPosition

    def get_object(self, queryset=None):
        obj = super(JobPositionDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/jobposition')


def employment_list_view(request):
    obj = Employment.objects.all()
    filter = EmploymentFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/employment.html', {'filter': filter})


class EmploymentCreateView(CreateView):
    model = Employment
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class EmploymentUpdateView(UpdateView):
    model = Employment
    form_class = EmploymentForm
    template_name = 'hospital/update_view/employ_update_view.html'


class EmploymentDeleteView(DeleteView):
    model = Employment

    def get_object(self, queryset=None):
        obj = super(EmploymentDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/employment')


def patient_list_view(request):
    obj = Patient.objects.all()
    filter = PatientFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/patient.html', {'filter': filter})


class PatientCreateView(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'hospital/update_view/employ_update_view.html'


class PatientDeleteView(DeleteView):
    model = Patient

    def get_object(self, queryset=None):
        obj = super(PatientDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/patient')


def bankaccount_list_view(request):
    obj = BankAccount.objects.all()
    filter = BankAccountFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/bankaccount.html', {'filter': filter})


class BankAccountCreateView(CreateView):
    model = BankAccount
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class BankAccountUpdateView(UpdateView):
    model = BankAccount
    form_class = BankAccountForm
    template_name = 'hospital/update_view/employ_update_view.html'


class BankAccountDeleteView(DeleteView):
    model = BankAccount

    def get_object(self, queryset=None):
        obj = super(BankAccountDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/bankaccount')


def appointment_list_view(request):
    obj = Appointment.objects.all()
    filter = AppointmentFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/appointment.html', {'filter': filter})


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'hospital/update_view/employ_update_view.html'


class AppointmentDeleteView(DeleteView):
    model = Appointment

    def get_object(self, queryset=None):
        obj = super(AppointmentDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/appointment')


def familydoctor_list_view(request):
    obj = FamilyDoctor.objects.all()
    filter = FamilyDoctorFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/familydoctor.html', {'filter': filter})


class FamilyDoctorCreateView(CreateView):
    model = FamilyDoctor
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class FamilyDoctorUpdateView(UpdateView):
    model = FamilyDoctor
    form_class = FamilyDoctorForm
    template_name = 'hospital/update_view/employ_update_view.html'


class FamilyDoctorDeleteView(DeleteView):
    model = FamilyDoctor

    def get_object(self, queryset=None):
        obj = super(FamilyDoctorDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/familydoctor')


def department_list_view(request):
    obj = Department.objects.all()
    filter = DepartmentFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/department.html', {'filter': filter})


class DepartmentCreateView(CreateView):
    model = Department
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'hospital/update_view/employ_update_view.html'


class DepartmentDeleteView(DeleteView):
    model = Department

    def get_object(self, queryset=None):
        obj = super(DepartmentDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/department')


def hospitalroom_list_view(request):
    obj = HospitalRoom.objects.all()
    filter = HospitalRoomFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/hospitalroom.html', {'filter': filter})


class HospitalRoomCreateView(CreateView):
    model = HospitalRoom
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class HospitalRoomUpdateView(UpdateView):
    model = HospitalRoom
    form_class = HospitalRooForm
    template_name = 'hospital/update_view/employ_update_view.html'


class HospitalRoomDeleteView(DeleteView):
    model = HospitalRoom

    def get_object(self, queryset=None):
        obj = super(HospitalRoomDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/hospitalroom')


def residence_list_view(request):
    obj = Residence.objects.all()
    filter = ResidenceFilter(request.GET, queryset=obj)
    return render(request, 'hospital/list_view/residence.html', {'filter': filter})


class ResidenceCreateView(CreateView):
    model = Residence
    fields = '__all__'
    template_name = 'hospital/form/base_from.html'


class ResidenceUpdateView(UpdateView):
    model = Residence
    form_class = ResidenceForm
    template_name = 'hospital/update_view/employ_update_view.html'


class ResidenceDeleteView(DeleteView):
    model = Residence

    def get_object(self, queryset=None):
        obj = super(ResidenceDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            messages.error(request, "You can not delete this row.")
            return HttpResponseRedirect('/hospital/residence')
