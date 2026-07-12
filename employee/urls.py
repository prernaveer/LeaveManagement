from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # Employee CRUD
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_add, name='employee_add'),
    path('update/<int:pk>/', views.employee_update, name='employee_update'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),

    #Leave CRUD
    path('leave/', views.leave_list, name='leave_list'),
    path('leave/add/', views.leave_add, name='leave_add'),
    path('leave/update/<int:pk>/', views.leave_update, name='leave_update'),
    path('leave/delete/<int:pk>/', views.leave_delete, name='leave_delete'),

    # ===========================
# Employee REST APIs
# ===========================

path('api/employees/', views.EmployeeListAPI.as_view(), name='employee-api'),

path('api/employees/<int:pk>/', views.EmployeeDetailAPI.as_view(), name='employee-detail-api'),

# ===========================
# Leave REST APIs
# ===========================

path('api/leaves/', views.LeaveListAPI.as_view(), name='leave-api'),

path('api/leaves/<int:pk>/', views.LeaveDetailAPI.as_view(), name='leave-detail-api'),
]