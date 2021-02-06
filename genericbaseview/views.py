from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from genericbaseview.models import Employee

class AddEmployee(CreateView):
    model = Employee
    template_name = 'addemp.html'
    fields = '__all__'
    success_url = reverse_lazy('list')

class UpdateEmployee(UpdateView):
    model = Employee
    template_name = 'updateemp.html'
    fields = '__all__'
    success_url = reverse_lazy('list')

class DeleteEmployee(DeleteView):
    model = Employee
    template_name = 'deleteemp.html'
    success_url = reverse_lazy('list')

    def delete(self, request, *args, **kwargs):
        eid = kwargs.get('pk')
        emp = Employee.objects.filter(eid=eid).first()
        emp.active = 'N'
        emp.save()
        return HttpResponseRedirect(DeleteEmployee.success_url)

class FetchAllEmployee(ListView):
    model = Employee
    template_name = 'allemp.html'