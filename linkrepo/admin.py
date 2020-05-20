from django.contrib import admin
from .models import Link


class LinkController(admin.ModelAdmin):
    list_display = ["__str__", "create", "updated"]
    search_fields = ('title',)

    class Meta:
        model = Link


# Register your models here.
admin.site.register(Link, LinkController)
