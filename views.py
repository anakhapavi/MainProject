from django.shortcuts import render
from vaccination.models import Vaccination

# Create your views here.
from vaccination_request.models import VaccinationRequest

def vaccinationrequest(request,idd):
    if request.method=="POST":
        obj=VaccinationRequest()
        obj.request="requested"
        obj.date=request.POST.get('dat')
        obj.time=request.POST.get('tim')
        obj.u_id="1"
        obj.vc_id=idd
        obj.save()
    return render(request,'vaccination_request/view requst.html')


def aprove(request,idd):
    obj=VaccinationRequest.objects.get(v_id=idd)
    obj.status='aprove'
    obj.save()
    return vaccinationrequest(request)

def rjct(request,idd):
    obj=VaccinationRequest.objects.get(v_id=idd)
    obj.status='reject'
    obj.save()
    return vaccinationrequest(request)

def status(request):
    obj=VaccinationRequest.objects.all()
    context={
        'objval':obj
    }
    return render(request, 'vaccination_request/view status.html', context)
def requst(request):
    obj=VaccinationRequest.objects.all()
    context={
        'objval':obj
    }
    return render(request, 'vaccination_request/viewvaccinerequest.html', context)

def reject(request,idd):
    obj=VaccinationRequest.objects.get(v_id=idd)
    obj.status='reject'
    obj.save()
    return requst(request)

def acptt(request,idd):
    obj=VaccinationRequest.objects.get(v_id=idd)
    obj.status='acept'
    obj.save()
    return requst(request)



