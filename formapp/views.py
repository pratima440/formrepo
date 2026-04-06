from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.http import HttpResponse
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show/')
    else:
        form = EmployeeForm()
    return render(request,'add.html',{'form':form})

def show_employee(request):
    data = Employee.objects.all()
    return render(request,'show.html',{'data':data})

def edit_employee(request,id):
    emp=Employee.objects.get(id=id)
    form=EmployeeForm(instance=emp)
    return render(request,'edit.html',{'form':form})

def update_employee(request,id):
    emp=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=emp)
    if form.is_valid():
        form.save()
        return redirect('/show/')

def delete_employee(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/show/')
def home(request):
    return HttpResponse("Hello,your Django site is live")
