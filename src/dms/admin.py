from django.contrib import admin
from .models import Switch, Controller


@admin.register(Switch, Controller)
class AuthorAdmin(admin.ModelAdmin):
    pass
