from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('shortner_app.urls', namespace='shortner_app'))
]
