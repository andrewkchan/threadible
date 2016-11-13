from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .api import *

@csrf_exempt
def create_workspace(request):
    if request.method == "POST" and 'name' in request.POST:
        return JsonResponse({'workspace_id' : Workspace(request.POST['name']).workspace_id})
    return HttpResponseBadRequest("This api page takes a POST with 'name'.")

@csrf_exempt
def edit_cell(request):
    '''
    @param request - A JSON of the form {workspace_id:(INT), cell_id:(INT), code:(TEXT)}
    
    Updates the corresponding cell's contents in the DB, creating a new entry if
    the cell does not already exist in the DB (indicated by cell_id=-1).
    In the HTTP response, returns a JSON of the form
    {cell_id:(INT), output:(OUTPUT_JSON)}, with OUTPUT_JSON specified by:
    
    output == {type:(STRING, "terminal" if terminal output, "image" if graphical output), data:(STRING, stdout or the image URL)}
    
    The output is determined by the execution of the new cell code.
    '''
    return HttpResponse(request.method + " " + request.POST['workspace_id'])
    if request.method == "POST" and 'workspace_id' in request.POST and 'cell_id' in request.POST and 'code' in request.POST:
        return edit_cell_content(request.POST['workspace_id'], request.POST['cell_id'], request.POST['code'])
    return HttpResponseBadRequest("This api page takes a POST with 'workspace_id', cell_id', 'code'.")