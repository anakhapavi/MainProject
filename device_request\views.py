from django.shortcuts import render

# Create your views here.
from device_request.models import DeviceRequest
def device_requestn_mnage(request):
    obj=DeviceRequest.objects.all()
    context={
        'objval':obj
    }
    return render(request,'device_request/viewdevicerequest.html',context)
def aprove(request,idd):
    obj=DeviceRequest.objects.get(d_id=idd)
    obj.status='aprove'
    obj.save()
    return device_requestn_mnage(request)
def reject(request,idd):
    obj=DeviceRequest.objects.get(d_id=idd)
    obj.status='reject'
    obj.save()
    return device_requestn_mnage(request)
def device_request(request):
    obj=DeviceRequest.objects.all()
    context={
        'objval':obj
    }
    return render(request,'device_request/viewrequest.html',context)
def req(request,idd):
    obj=DeviceRequest.objects.get(d_id=idd)
    obj.status='requsted'
    obj.save()
    return device_request(request)
