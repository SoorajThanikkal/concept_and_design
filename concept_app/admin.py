from django.contrib import admin

# Register your models here.
from .import models

admin.site.site_header = "C2D Admin Portal"
admin.site.site_title = "C2d Admin"
admin.site.index_title = "Welcome to C2D Admin Dashboard"


admin.site.register(models.Projects)