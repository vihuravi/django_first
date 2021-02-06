from django.shortcuts import render
from funbaseview.models import Employee, Address


# Create your views here.

def welcome_page_emp(req):
    return render(request=req, template_name='emp.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.get_dummy_employee(),
        'adrlist': Address.objects.all(),
        'msg': ''
    })


def add_update_employee(req):
    msg = ''
    if req.method == 'POST':
        data = req.POST
        if data.get('empid'):
            dbemp = Employee.objects.filter(eid=data.get('empid')).first()
        emp = Employee(eid=data.get('empid'), name=data.get('empname'), age=data.get('empage'),
                       email=data.get('empemail'),
                       salary=data.get('empsal'), role=data.get('emprole'))
        adrlist = [Address.objects.filter(aid=int(adrid)).first() for adrid in data.getlist('adr')]
        if emp.eid and emp.name and emp.age and emp.email and emp.role and emp.salary and emp.adr:
            if dbemp:
                dbemp.name = emp.name
                dbemp.age = emp.age
                dbemp.email = emp.email
                dbemp.salary = emp.salary
                dbemp.role = emp.role
                dbemp.adr.clear()
                dbemp.adr.add(*adrlist)
                dbemp.save()
                msg = f'Employee {dbemp.eid} update successfully..!'
            else:
                emp.save()
                emp.adr.add(*adrlist)
                msg = f'Employee {emp.eid} added successfully..!'
        else:
            msg = 'Invalid credentials..!'
    return render(request=req, template_name='emp.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.get_dummy_employee(),
        'adrlist': Address.objects.all(),
        'msg': msg
    })


def edit_employee(req, eid):
    dbemp = Employee.objects.filter(eid=eid).first()
    if dbemp:
        return render(request=req, template_name='emp.html', context={
            'emplist': Employee.objects.all(),
            'emp': dbemp,
            'adrlist': Address.objects.all(),
            'msg': ''
        })
    return render(request=req, template_name='emp.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.get_dummy_employee(),
        'adrlist': Address.objects.all(),
        'msg': f'Employee {eid} not found..!'
    })


def delete_employee(req, eid):
    msg = ''
    dbemp = Employee.objects.filter(eid=eid).first()
    if dbemp:
        dbemp.delete()
        msg = f'Employee {eid} delete successfully..!'
    return render(request=req, template_name='emp.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.get_dummy_employee(),
        'adrlist': Address.objects.all(),
        'msg': msg
    })



def add_update_address(req):
    msg = ''
    if req.method == 'POST':
        data = req.POST
        if data.get('adrid'):
            dbadr = Address.objects.filter(aid=data.get('adrid')).first()
        adr = Address(aid=data.get('adrid'), city=data.get('adrcity'), state=data.get('adrstate'),
                      pincode=data.get('adrpincode'))
        if adr.aid and adr.city and adr.state and adr.pincode:
            if dbadr:
                dbadr.city = adr.city
                dbadr.state = adr.state
                dbadr.pincode = adr.pincode
                dbadr.save()
                msg = f'Address {dbadr.aid} update successfully..!'
            else:
                adr.save()
                msg = f'Address {adr.aid} added successfully..!'
        else:
            msg = 'Invalid credentials..!'
    return render(request=req, template_name='emp.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.get_dummy_employee(),
        'adrlist': Address.objects.all(),
        'msg': msg,
        'adr': Address.get_dummy_address()
    })


def edit_address(req, aid):
    return render(request=req, template_name='emp.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.get_dummy_employee(),
        'adrlist': Address.objects.all(),
        'msg': '',
        'adr': Address.objects.filter(aid=aid).first()
    })


def delete_address(req, aid):
    msg = ''
    dbadr = Address.objects.filter(aid=aid).first()
    if dbadr:
        dbadr.delete()
        msg = f'Address {aid} delete successfully..!'
    return render(request=req, template_name='emp.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.get_dummy_employee(),
        'adrlist': Address.objects.all(),
        'msg': msg,
        'adr': Address.get_dummy_address()
    })
