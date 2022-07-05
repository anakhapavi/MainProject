from django.shortcuts import render

# Create your views here.
from vaccination.models import Vaccination
def vaccination(request):
    if request.method=="POST":
        obb=Vaccination()
        obb.name=request.POST.get('nam')
        obb.availability=request.POST.get('avail')
        obb.date=request.POST.get('dat')
        obb.time=request.POST.get('tim')
        obb.venue=request.POST.get('ven')
        obb.save()

    return render(request,'vaccination/vaccinedetails.html')


def vv(req):
    o=Vaccination.objects.all()
    con={
        'ss':o
    }
    return render(req,'vaccination/viewvaccinationdetails.html',con)


