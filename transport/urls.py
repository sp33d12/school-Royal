from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Manager
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/students/', views.manager_students, name='manager_students'),
    path('manager/students/add/', views.manager_student_form, name='manager_student_add'),
    path('manager/students/<int:pk>/edit/', views.manager_student_form, name='manager_student_edit'),
    path('manager/students/<int:pk>/delete/', views.manager_student_delete, name='manager_student_delete'),
    path('manager/drivers/', views.manager_drivers, name='manager_drivers'),
    path('manager/drivers/<int:pk>/delete/', views.manager_driver_delete, name='manager_driver_delete'),
    path('manager/supervisors/', views.manager_supervisors, name='manager_supervisors'),
    path('manager/supervisors/<int:pk>/delete/', views.manager_supervisor_delete, name='manager_supervisor_delete'),
    path('manager/employees/', views.manager_employees, name='manager_employees'),
    path('manager/employees/<int:pk>/delete/', views.manager_employee_delete, name='manager_employee_delete'),
    path('manager/import/', views.manager_import, name='manager_import'),
    path('manager/template/', views.download_template, name='excel_template'),

    # Single-page manager
    path('manager/', views.manager_page, name='manager_page'),
    path('manager/change-password/', views.change_password, name='change_password'),
    path('manager/backup/', views.backup_database, name='backup_database'),

    # Employee / Search
    path('search/', views.employee_search, name='employee_search'),
    path('employee/add-student/', views.employee_add_student, name='employee_add_student'),
    path('api/search/', views.api_search, name='api_search'),
    path('api/student/<int:pk>/', views.api_student, name='api_student'),
    path('api/student_raw/<int:pk>/', views.api_student_raw, name='api_student_raw'),
]
