from django.contrib import admin

# Register your models here.
from .models import Note

class NotesAdmin(admin.ModelAdmin):
    list_filter = ["active"]
    list_display = ["title" , "created" , "active"]
    search_fields = ['title','content']


admin.site.register(Note , NotesAdmin)
