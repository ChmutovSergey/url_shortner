from django.contrib import admin

from .models import Urls


@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('md_url', 'short_url', 'http_url', 'pub_date', )
    ordering = ('-pub_date', )
