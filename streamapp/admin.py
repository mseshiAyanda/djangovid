from django.contrib import admin
from .models import Cam
# Register your models here.

class CamAdmin(admin.ModelAdmin):
    list_display    = ("id","cam_name","framecount","is_webcam")
    search_fields   = ("cam_name",)
    list_editable   = ()
    readonly_fields = ()
    filter_horizntal= ()
    list_filter     = ("is_webcam",)
    fieldsets       = ()

admin.site.register(Cam,CamAdmin)
