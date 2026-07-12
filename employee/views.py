from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Employee, Leave
from .forms import EmployeeForm, LeaveForm

from rest_framework import generics
from .serializers import EmployeeSerializer, LeaveSerializer


# View all employees with Search
def employee_list(request):
    query = request.GET.get('q')

    employees = Employee.objects.all()

    if query:
        employees = employees.filter(
            Q(name__icontains=query) |
            Q(employee_id__icontains=query)
        )

    return render(
        request,
        'employee/employee_list.html',
        {'employees': employees}
    )


# Add employee
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employee/employee_form.html', {'form': form})


# Update employee
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee/employee_form.html', {'form': form})


# Delete employee
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})

# Create your views here.

# View all leave applications
# View all leave applications with Filters
def leave_list(request):

    status = request.GET.get('status')
    leave_type = request.GET.get('leave_type')

    leaves = Leave.objects.all()

    if status:
        leaves = leaves.filter(status=status)

    if leave_type:
        leaves = leaves.filter(leave_type=leave_type)

    return render(
        request,
        'employee/leave_list.html',
        {
            'leaves': leaves
        }
    )


# Apply Leave
def leave_add(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveForm()

    return render(request, 'employee/leave_form.html', {'form': form})


# Update Leave
def leave_update(request, pk):
    leave = get_object_or_404(Leave, pk=pk)

    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveForm(instance=leave)

    return render(request, 'employee/leave_form.html', {'form': form})


# Delete Leave
def leave_delete(request, pk):
    leave = get_object_or_404(Leave, pk=pk)

    if request.method == 'POST':
        leave.delete()
        return redirect('leave_list')

    return render(request, 'employee/leave_confirm_delete.html', {'leave': leave})

# Dashboard
def dashboard(request):

    context = {
        'total_employees': Employee.objects.count(),
        'total_leaves': Leave.objects.count(),
        'approved_leaves': Leave.objects.filter(status='Approved').count(),
        'pending_leaves': Leave.objects.filter(status='Pending').count(),
        'rejected_leaves': Leave.objects.filter(status='Rejected').count(),
    }

    return render(request, 'employee/dashboard.html', context)





# ===========================
# Employee REST API
# ===========================

class EmployeeListAPI(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# ===========================
# Leave REST API
# ===========================

class LeaveListAPI(generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer


class LeaveDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer