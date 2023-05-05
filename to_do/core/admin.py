from django.contrib import admin
from .models import Tarefa

class TarefasModelAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'inicio', 'fim', 'status')
    date_hierarchy = 'inicio'
    search_fields = ('tarefa', 'inicio')

admin.site.register(Tarefa, TarefasModelAdmin)

