from django.shortcuts import render
from django.http import HttpResponse
from threeApp.models import AccessRecord,Webpage,Topic

# Create your views here.
def index(request):
    web_list = AccessRecord.objects.order_by('-date')
    my_dict={
        'access_records':web_list
    }
    return render(request,'twoApp/indexnew.html',context=my_dict)