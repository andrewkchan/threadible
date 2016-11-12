from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def eval(request):
    if request.method == "POST":
        return HttpResponse(str(eval(request.POST['input'])))
    return HttpResponse("Hi! Please send a POST with key 'input'. {}".format(request))