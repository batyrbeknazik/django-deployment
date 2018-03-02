from django.shortcuts import render
from django.http import HttpResponse
from users.models import Names

# Create your views here.
def index(request):
    names_list = Names.objects.order_by('name')
    my_dict = {
        'access': names_list
    }

    return render(request,'users.html',context=my_dict)