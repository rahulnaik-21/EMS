from django.shortcuts import render,redirect
from .models import Employee , Department
from .form import EmployeeForm,DepartmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import (
    user_passes_test
)

from .utils import is_admin

def home(request):
    return render (request, 'home.html')


@login_required
def departments(request):
    dept_list = Department.objects.all()
    return render(request,'departments.html',{'departments': dept_list})

@login_required
def employees(request):
    emp_list = Employee.objects.all()
    return render(request,'employees.html',{'employees': emp_list})


@login_required
@user_passes_test(is_admin)
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/departments/')
    else:
        form=DepartmentForm()
    return render(request,'add_department.html',{'form':form})



@login_required
@user_passes_test(is_admin)
def add_employee(request):
    # departments = Department.objects.all()
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employees/')
    else:
        form=EmployeeForm()
    # return render(request,'add_employee.html',{'departments': departments})
    return render(request,'add_employee.html',{'form':form})



@login_required
@user_passes_test(is_admin)
def edit_employee(request, id):
    emp = Employee.objects.get(id=id)
    
    if request.method == 'POST':
        form =EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/employees/')
    else:        
        form=EmployeeForm(instance=emp)
    
    return render(request,'edit_employee.html',{'form':form})
# here we are not sent department because internally django has took employee model so there is foreign involed in department .


@login_required
@user_passes_test(is_admin)
def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    # we simple use delete option
    return redirect('/employees/')


@login_required
@user_passes_test(is_admin)
def edit_department(request, id):
    dept = Department.objects.get(id=id)
    if request.method == 'POST':
        form = DepartmentForm( request.POST,instance=dept)
        if form.is_valid():
            form.save()

        return redirect('/departments/' )
    return render(request,'edit_department.html',{'form':form})



@login_required
@user_passes_test(is_admin)
def delete_department(request, id):
    dept = Department.objects.get(id=id)
    dept.delete()
    return redirect('/departments/')

# def home(request):

#     print(request.user)

#     return render(
#         request,
#         'home.html'
#     )