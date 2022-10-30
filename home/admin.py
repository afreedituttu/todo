from django.contrib import admin
from .models import tasks
# Register your models here.

class TasksView(admin.ModelAdmin):
    list_display = ['name','money']

admin.site.register(tasks,TasksView)
