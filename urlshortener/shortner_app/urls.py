from django.conf.urls import include, url
from django.urls import path


path(r'', include('shortner_app.urls', namespace='shortner_app'))

urlpatterns = [
    path(r'^$', 'index', name='home'),
    path(r'^(?P&lt;short_id&gt;\w{6})$', 'redirect_original', name='redirectoriginal'),
    path(r'^makeshort/$', 'short_url', name='shortenurl'),
]
