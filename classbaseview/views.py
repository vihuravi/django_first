from django.shortcuts import render,reverse
from django.views import View
from classbaseview.models import *
# from django.views.generic import CreateView,UpdateView,DeleteView,ListView

# Create your views here.

# class AddEmp(CreateView):
#     model = None
#     template_name = None
#     success_url = None
#     # fields = ('name','age')
#     extra_context = 'name'


class CrudEmployeeOps(View):

    def get(self, req, *args, **kwargs):
        msg = ''
        dbemp = Employee.get_dummy_employee()
        emplist = Employee.objects.all()
        if 'delete' in req.path:
            emp = Employee.objects.filter(eid=kwargs.get('pk')).first()
            emp.delete()
            msg = 'Employee delete Successfully..!'
        elif 'edit' in req.path:
            dbemp = Employee.objects.filter(eid=kwargs.get('pk')).first()
        return render(req, 'sample.html', {'msg': msg, 'emplist': emplist, 'emp': dbemp})

    def post(self, req, *args, **kwargs):
        msg = ''
        emplist = Employee.objects.all()
        data = req.POST
        dbemp = Employee.objects.filter(eid=int(data.get('eid'))).first()
        if dbemp:
            dbemp.name = data.get('ename')
            dbemp.age = data.get('eage')
            dbemp.salary = data.get('esal')
            dbemp.save()
            msg = 'Employee update Successfully..!'
        else:
            emp = Employee(eid=data.get('eid'),name=data.get('ename'),age=data.get('eage'),salary=data.get('esal'))
            emp.save()
            msg = 'Employee added Successfully..!'
        return render(req,'sample.html', {'msg': msg, 'emplist': emplist, 'emp': dbemp})