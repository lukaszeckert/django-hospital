from django.urls import path
from . import views

urlpatterns = [
   path('', views.employ_list_view, name='index'),
   # path('search/', views.search, name='search'),

    path('employ/', views.employ_list_view, name='employ'),
    path('employ/<int:pk>/', views.EmployUpdateView.as_view(success_url="/hospital/employ/"), name='employ_details'),
    path('employ/add/', views.EmployCreateView.as_view(success_url="/hospital/employ/"), name='employ_add'),
    path('employ_delete/<int:pk>)', views.EmployDeleteView.as_view(success_url="/hospital/employ/"), name='employ_delete'),
    path('employ/raise', views.employ_raise_view, name='employ_raise'),

    path('jobposition/', views.jobposition_list_view, name='jobposition'),
    path('jobposition/<int:pk>/', views.JobPositionUpdateView.as_view(success_url="/hospital/jobposition/"),
         name='jobposition_details'),
    path('jobposition/add/', views.JobPositionCreateView.as_view(success_url="/hospital/jobposition/"),
         name='jobposition_add'),
    path('jobposition_delete/<int:pk>)', views.JobPositionDeleteView.as_view(success_url="/hospital/jobposition/"),
         name='jobposition_delete'),

    path('employment/', views.employment_list_view, name='employment'),
    path('employment/<int:pk>/', views.EmploymentUpdateView.as_view(success_url="/hospital/employment/"),
         name='employment_details'),
    path('employment/add/', views.EmploymentCreateView.as_view(success_url="/hospital/employment/"),
         name='employment_add'),
    path('employment_delete/<int:pk>)', views.EmploymentDeleteView.as_view(success_url="/hospital/employment/"),
         name='employment_delete'),

    path('patient/', views.patient_list_view, name='patient'),
    path('patient/<int:pk>/', views.PatientUpdateView.as_view(success_url="/hospital/patient/"), name='patient_details'),
    path('patient/add/', views.PatientCreateView.as_view(success_url="/hospital/patient/"), name='patient_add'),
    path('patient_delete/<int:pk>)', views.PatientDeleteView.as_view(success_url="/hospital/patient/"),
         name='patient_delete'),

    path('patient/', views.patient_list_view, name='patient'),
    path('patient/<int:pk>/', views.PatientUpdateView.as_view(success_url="/hospital/patient/"), name='patient_details'),
    path('patient/add/', views.PatientCreateView.as_view(success_url="/hospital/patient/"), name='patient_add'),
    path('patient_delete/<int:pk>)', views.PatientDeleteView.as_view(success_url="/hospital/patient/"),
         name='patient_delete'),

    path('bankaccount/', views.bankaccount_list_view, name='bankaccount'),
    path('bankaccount/<int:pk>/', views.BankAccountUpdateView.as_view(success_url="/hospital/bankaccount/"),
         name='bankaccount_details'),
    path('bankaccount/add/', views.BankAccountCreateView.as_view(success_url="/hospital/bankaccount/"),
         name='bankaccount_add'),
    path('bankaccount_delete/<int:pk>)', views.BankAccountDeleteView.as_view(success_url="/hospital/bankaccount/"),
         name='bankaccount_delete'),

    path('appointment/', views.appointment_list_view, name='appointment'),
    path('appointment/(<int:pk>/', views.AppointmentUpdateView.as_view(success_url="/hospital/appointment/"),
         name='appointment_details'),
    path('appointment/add/', views.AppointmentCreateView.as_view(success_url="/hospital/appointment/"),
         name='appointment_add'),
    path('appointment_delete/<int:pk>)', views.AppointmentDeleteView.as_view(success_url="/hospital/appointment/"),
         name='appointment_delete'),

    path('familydoctor/', views.familydoctor_list_view, name='familydoctor'),
    path('familydoctor/(<int:pk>/', views.FamilyDoctorUpdateView.as_view(success_url="/hospital/familydoctor/"),
         name='familydoctor_details'),
    path('familydoctor/add/', views.FamilyDoctorCreateView.as_view(success_url="/hospital/familydoctor/"),
         name='familydoctor_add'),
    path('familydoctor_delete/<int:pk>)', views.FamilyDoctorDeleteView.as_view(success_url="/hospital/familydoctor/"),
         name='familydoctor_delete'),

    path('department/', views.department_list_view, name='department'),
    path('department/(<int:pk>/', views.DepartmentUpdateView.as_view(success_url="/hospital/department/"),
         name='department_details'),
    path('department/add/', views.DepartmentCreateView.as_view(success_url="/hospital/department/"),
         name='department_add'),
    path('department_delete/<int:pk>)', views.DepartmentDeleteView.as_view(success_url="/hospital/department/"),
         name='department_delete'),

    path('hospitalroom/', views.hospitalroom_list_view, name='hospitalroom'),
    path('hospitalroom/(<int:pk>/', views.HospitalRoomUpdateView.as_view(success_url="/hospital/hospitalroom/"),
         name='hospitalroom_details'),
    path('hospitalroom/add/', views.HospitalRoomCreateView.as_view(success_url="/hospital/hospitalroom/"),
         name='hospitalroom_add'),
    path('hospitalroom_delete/<int:pk>)', views.HospitalRoomDeleteView.as_view(success_url="/hospital/hospitalroom/"),
         name='hospitalroom_delete'),

    path('residence/', views.residence_list_view, name='residence'),
    path('residence/(<int:pk>/', views.ResidenceUpdateView.as_view(success_url="/hospital/residence/"),
         name='residence_details'),
    path('residence/add/', views.ResidenceCreateView.as_view(success_url="/hospital/residence/"), name='residence_add'),
    path('residence_delete/<int:pk>)', views.ResidenceDeleteView.as_view(success_url="/hospital/residence/"),
         name='residence_delete'),


]

