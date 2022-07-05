from django.shortcuts import render

# Create your views here.
from user.models import User
from login.models import Login
def user(request):
    if request.method=="POST":
        obb=User()
        obb.username=request.POST.get('usrname')
        obb.password=request.POST.get('pass')
        obb.name=request.POST.get('nam')
        obb.address=request.POST.get('adds')
        obb.gender=request.POST.get('g')
        obb.age=request.POST.get('age')
        obb.phone_no=request.POST.get('phone')
        obb.email=request.POST.get('mail')
        obb.save()
    return render(request,'user/registeruser.html')
def view_user(request):
    obj=User.objects.all()
    context={
        'objval':obj
    }
    return render(request,'user/viewuser.html',context)

def aprove(request,idd):
    obj=User.objects.get(u_id=idd)
    obj.status='aprove'
    obj.save()
    ob = Login()
    ob.username = obj.username
    ob.password = obj.password
    ob.type = "user"
    ob.u_id= obj.u_id
    ob.save()
    return view_user(request)

def reject(request,idd):
    obj=User.objects.get(u_id=idd)
    obj.status='reject'
    obj.save()
    return view_user(request)
