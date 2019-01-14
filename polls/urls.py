from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    path('employees/', views.employees, name='employees'),
    path('employees/(<int:pk>/', views.EmployUpdateView.as_view(success_url="/polls/employees/"), name='hospitalstaff_details'),
    path('employ/add/',views.EmpolyCreateView.as_view(success_url="/polls/employees/"), name='employ_add'),
    path('employ_delete/<int:pk>)',views.EmployDeleteView.as_view(success_url="/polls/employees/"), name='HospitalStaff_delete'),

    path('job_position/', views.job_position, name='job_position'),
    path('position/add', views.JobPositionCreateView.as_view(success_url='/polls/'), name='position_add'),

    path('employment/add', views.EmploymentCreateView.as_view(success_url='/polls/'), name='employment_add')
]

