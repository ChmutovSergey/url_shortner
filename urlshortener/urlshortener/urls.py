from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('shortner_app.urls', namespace='shortner_app'))
]
