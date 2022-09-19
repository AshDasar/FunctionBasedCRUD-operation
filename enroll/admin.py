from django.contrib import admin

from .models import SaveStudentData

# Register your models here.
@admin.register(SaveStudentData)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','password')
