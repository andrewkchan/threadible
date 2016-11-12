from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .api import *

@csrf_exempt
def eval_(request):
    if request.method == "POST" and 'inposT' in request.POST:
        return HttpResponse(str(eval(request.POST['inposT'])))
    return HttpResponse("This api page takes a POST with 'inposT'. {}".format(request))

@csrf_exempt
def create_workspace(request):
    if request.method == "POST" and 'name' in request.POST:
        Workspace(request.POST['name'])
        return HttpResponse("Created new workspace " + request.POST['name'] + ".")
    return HttpResponse("This api page takes a POST with 'name'. {}".format(request))

@csrf_exempt
def create_cell(request):
    if request.method == "POST" and 'workspace_id' in request.POST:
        cell = Cell(request.POST['workspace_id'])
        return HttpResponse(cell.cell_id)
    return HttpResponse("This api page takes a POST with 'workspace_id', 'code'. {}".format(request))

@csrf_exempt
def edit_cell(request):
    if request.method == "POST" and 'cell_id' in request.POST and 'code' in request.POST:
        edit_cell_content(request.POST['cell_id'], request.POST['code'])
        return HttpResponse("Edited cell " + request.POST['cell_id'] + ".")
    return HttpResponse("This api page takes a POST with 'cell_id', 'code'. {}".format(request))

def eval_cell(request):
    if request.method == "GET" and 'cell_id' in request.GET:
        return HttpResponse(str(eval(request.GET['name'])))
    return HttpResponse("This api page takes a GET with 'cell_id'. {}".format(request))