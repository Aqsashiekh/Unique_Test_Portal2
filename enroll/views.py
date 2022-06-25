from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect 
from .forms import StudentRegistration
from .models import User

# Create your views here.

# This function will add new Item and Show All Items
def addstudent(request):
  if request.method == 'POST':
    fm = StudentRegistration(request.POST)
    if fm.is_valid():
      nm = fm.cleaned_data['user_name']
      pw = fm.cleaned_data['password']
      ut = fm.cleaned_data['user_type']
      cl= fm.cleaned_data['class_id']
      pn  = fm.cleaned_data['phone_number']
      em = fm.cleaned_data['email']
      ad = fm.cleaned_data['address']
      reg = User(user_name=nm, password=pw, user_type=ut, class_id=cl, phone_number=pn, email=em, address=ad)
      reg.save()
      fm = StudentRegistration()
  else:
      fm = StudentRegistration()
  stud = User.objects.all()
  return render(request, 'enroll/addstudent.html', {'form':fm, 'stu':stud})

# This function will update/Edit

def updatestudent(request, id):
  if request.method == 'POST':
    pi = User.objects.get(pk=id)
    fm = StudentRegistration(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
  else:
    pi = User.objects.get(pk=id)
    fm = StudentRegistration(instance=pi)

  return render(request, 'enroll/updatestudent.html', {'form':fm})

#  This function will Delete
def deletestudent(request, id):
  if request.method == 'POST':
    pi = User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')




