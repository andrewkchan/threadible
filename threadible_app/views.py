from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

from django import forms

class InputForm(forms.Form):
   user = forms.CharField(max_length = 100)
   
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == "POST":
        return HttpResponse(str(eval(request.POST['code'])))
    return HttpResponse("Hi! Please send a POST with key 'code'. {}".format(request))