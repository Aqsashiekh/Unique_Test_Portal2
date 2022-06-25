from django.shortcuts import redirect, render, reverse
from django.shortcuts import HttpResponseRedirect
from .forms import _Class
from .model import class_model
from django.contrib import messages

# This function will add class
def add_class(request):
    if request.method == "POST":
        frm = _Class(request.POST)
        if frm.is_valid():
            class_name = frm.cleaned_data["class_name"]
            reg = class_model(class_name=class_name)
            reg.save()
            messages.add_message(request, messages.INFO, "your class delete successfully.")

            frm = _Class()

            return redirect(reverse("list_class"))
    else:
        frm = _Class()
        return render(request, "enroll/class/add_class.html", {"form": frm})


def list_class(request):
    class_list = class_model.objects.all()
    frm = _Class()

    return render(
        request, "enroll/class/list_class.html", {"class_list": class_list, "form": frm}
    )


#  This function will Delete
def delete_class(request, id):
    class_obj = class_model.objects.get(pk=id)
    class_obj.delete()
    messages.add_message(request, messages.INFO, {"title": "test", "text": "your class delete successfully."})

    return redirect(reverse("list_class"))


# this function show updateclass
def update_class(request, id):
    if request.method == "POST":
        class_obj = class_model.objects.get(pk=id)
        frm = _Class(request.POST, instance=class_obj)
        if frm.is_valid():
            frm.save()
            messages.add_message(request, messages.INFO, {"title": "test", "text": "your class delete successfully."})

        return redirect(reverse("list_class"))

    else:
        class_obj = class_model.objects.get(pk=id)
        frm = _Class(instance=class_obj)

    messages.add_message(request, messages.INFO, "your class delete successfully.")

    return render(request, "enroll/class/update_class.html", {"form": frm})
