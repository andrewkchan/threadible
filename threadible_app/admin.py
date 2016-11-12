from django.contrib import admin

# Register your models here.

from threadible_app.models import Comment, Workspace, WSUser, Cell

admin.site.register(Comment)
admin.site.register(Workspace)
admin.site.register(WSUser)
admin.site.register(Cell)