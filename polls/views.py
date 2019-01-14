from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django_tables2 import RequestConfig

from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.template import loader
from .filters import *
from django.contrib.auth.models import User
from django import forms
from django.forms import modelform_factory
from django.http import Http404, HttpResponseRedirect

from .models import *
from .forms import *


# Create your views here.
def index(request):
    template = loader.get_template('polls/index.html')

    return HttpResponse(template.render({}, request))


def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'polls/index.html', {'filter': user_filter})


# ---------------------------------
# employ

def employees(request):
    employees = HospitalStaff.objects.all()
    employees_filter = EmployeesFilter(request.GET, queryset=employees)
    return render(request, 'polls/list_view/employees.html', {'filter': employees_filter})


class EmpolyCreateView(CreateView):
    model = HospitalStaff
    fields = ['first_name', 'second_name', 'boss_id']


class EmployUpdateView(UpdateView):
    model = HospitalStaff
    form_class = EmployForm
    template_name = 'polls/update_view/employ_update_view.html'


class EmployDeleteView(DeleteView):
    model = HospitalStaff

    def get_object(self, queryset=None):
        obj = super(EmployDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            return HttpResponseRedirect('/polls/employees')


# -----------------------------------------------
def job_position(request):
    positions = JobPosition.objects.all()
    filter = JobPositionFilter(request.GET, queryset=positions)
    return render(request, 'polls/list_view/job_position.html', {'filter': filter})

class JobPositionCreateView(CreateView):
    model = JobPosition
    fields = '__all__'


class JobPositionUpdateView(UpdateView):
    model = JobPosition
    form_class = JobForm
    template_name = 'polls/employ_update_view.html'


class JobPositionDeleteView(DeleteView):
    model = JobPosition

    def get_object(self, queryset=None):
        obj = super(JobPositionDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            return HttpResponseRedirect('/polls/employees')

#----------------------------------------------------
class EmploymentCreateView(CreateView):
    model = Employment
    fields = '__all__'


class EmploymentUpdateView(UpdateView):
    model = Employment
    form_class = EmploymentForm
    template_name = 'polls/base_update_view.html'


class EmploymentDeleteView(DeleteView):
    model = Employment

    def get_object(self, queryset=None):
        obj = super(JobPositionDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except:
            return HttpResponseRedirect('/polls/employees')