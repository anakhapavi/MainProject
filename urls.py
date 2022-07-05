from django.conf.urls import url
from vaccination_request import views

urlpatterns = [
    url('^vaccination_request/(?P<idd>\w+)',views.vaccinationrequest,name="reqsttt"),
    url('^v_vaccination_request/',views.requst),
    url('^r_vaccination_request/',views.status),
    url('^accpt/(?P<idd>\w+)',views.acptt,name='acptt'),
    url('^accpt/(?P<idd>\w+)', views.reject, name='rjcttt'),
url('^drclr/(?P<idd>\w+)', views.rjct, name='aaaa'),
url('^aprove/(?P<idd>\w+)', views.aprove, name='bbbb')

]
