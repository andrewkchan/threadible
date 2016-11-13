from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Workspace(models.Model):
    name = models.TextField() #name of the workspace.
    created = models.DateTimeField(auto_now_add=True)

#A cell is an ipython notebook code cell with python code inside.
class Cell(models.Model):
    workspace_id = models.ForeignKey(Workspace)
    user_id = models.ForeignKey(User) #the original author of the cell.
    code = models.TextField() #the code snippet inside of the cell.
    created = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    user_id = models.ForeignKey(User) #the author of the comment.
    cell_id = models.ForeignKey(Cell) #comments are attached to a cell.
    text = models.CharField(max_length=255) #the text associated with the comment.
    created = models.DateTimeField(auto_now_add=True)

class WSUser(models.Model):
    '''
    An entry in table WSUsers creates a 1-1 relationship between a workspace and a given user.
    for example, a user can be an admin of a workspace. Then he/she will have a WSUser entry associating the user and the workspace
    he/she is an admin of.
    '''
    workspace_id = models.ForeignKey(Workspace) #the workspace in question.
    user_id = models.ForeignKey(User) #the user associated with the workspace.
    can_execute = models.BooleanField() #user can execute code snippets in the workspace
    can_write = models.BooleanField() #user has write access to the code in the workspace and can upload/delete files in the workspace
    is_admin = models.BooleanField() #user can change permissions of other users associated with the workspace
    