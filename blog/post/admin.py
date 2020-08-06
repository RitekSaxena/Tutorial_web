from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.Chapters)
admin.site.register(models.Videos)
admin.site.register(models.Content)