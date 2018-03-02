from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = { 'insert_me':'Hello i am from views.py','fuckthat':'hey i just tried'}
    return render(request, 'twoApp/index.html', context=my_dict)