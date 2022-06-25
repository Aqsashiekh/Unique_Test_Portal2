from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect 
from .forms import StudentRegistration
from .models import User

# Create your views here.

# This function will add new Item and Show All Items
def load_index(request):
  return render(request, 'enroll/index.html', {})

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




