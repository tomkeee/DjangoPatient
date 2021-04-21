from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import Http404,HttpResponseRedirect

from .models import Patient
from .forms import PatientForm

# Create your views here.
def patient_create_view(request):
    if request.method=="POST":
        form=PatientForm(request.POST or None)
   
        if form.is_valid():
            form.save()
            form=PatientForm()
        return HttpResponseRedirect("/patient")
        
    else:
       form=PatientForm()
    context={
        "form":form
    }
    return render(request,"create_form.html",context)


def patient_detail_view(request,id):
    try:
        obj=Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        raise Http404
    context={"object":obj}
    return render(request,"patient_detail.html",context)


def patient_list_view(request):
    queryset=Patient.objects.all()
    context = {
        "content":queryset
    }
    return render(request,"patient_list.html",context)

def patient_delete_view(request,id):
    obj=Patient.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return render(request,"patient_delete_success.html",{})
    return render(request,"patient_delete.html",{})

def delete_suc(request):
    obj=Patient.objects.get()
    context={
        "object":obj
    }
    return render(request,"patient_delete_success.html",context)
