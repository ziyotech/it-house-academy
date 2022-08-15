from django.contrib import admin
from . import models

admin.site.register(models.CustomUser)
admin.site.register(models.Portfolio)
admin.site.register(models.Contact)
admin.site.register(models.Category_courses)
