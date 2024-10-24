from django.shortcuts import render
from .models import Student
# Create your views here.
def show_file(request):
    return render (request,"index.html")
def show_form(request):
    return render(request,"stud_form.html")
def save_student(request):
    id_no=request.POST.get('id')
    name=request.POST.get('name')
    course=request.POST.get('course')
    fee=request.POST.get('fee')
    s=Student(id=id_no,name=name,course=course,fee=fee)
    s.save
    return render(request,"stud_form.html",{"save_message":"student saved sucess"})
def view_all(request):
    query_set=Student.objects.all()
    return render(request,"view_all.html",{"qs":query_set})
def delete(request):
    return render(request,"delete.html")
def delete_std(request):
    id=request.POST.get('id')
    t=Student.objects.filter(id=id)
    if t[0]!=0:
        return render(request,"index.html",{'del_message':'delete success'})
    else:
        return render(request,"index.html",{'del_message':'std not exist!!!'})

