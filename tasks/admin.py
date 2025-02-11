from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# esto me muestra el nombre del titulo en el admin
admin.site.register(Task, TaskAdmin)
