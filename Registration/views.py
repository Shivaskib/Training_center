from django.shortcuts import render
from django.http import HttpResponse
from Registration import Course_Batch_Student

# Create your views here.

def index(requests):
    return HttpResponse("<h1>Welcome to Prime Intuit Registration</h1>")
def Home(requests):
#return HttpResponse("<h1>Welcome to Prime Intuit Registration</h1>")
#    my_dict = {'Insert_Me': "I am a text from Registration/Views.py"}
    batch_list = Batch.objects.order_by('batch_ID')
    data_dict = {'access_record':batch_list,'Insert_Me':"I am a text from Registration/Views.py"}
    return render(requests, 'Registration/index.html', context= data_dict)
