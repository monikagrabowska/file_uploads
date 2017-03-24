from django.contrib import admin

from .models import Upload, File

class FileAdminInline(admin.StackedInline):
    model = File
    extra = 1
 
class UploadAdmin(admin.ModelAdmin):
    inlines = [FileAdminInline]

admin.site.register(Upload, UploadAdmin)                                                                   
