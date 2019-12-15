from django.contrib import admin

from .models import Urls


@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'http_url', 'pub_date', 'count')
    ordering = ('-pub_date', )