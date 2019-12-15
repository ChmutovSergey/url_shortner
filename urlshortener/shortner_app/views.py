import json
import random
import string
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Urls


def index(request):

    return render(request, 'shortner_app/index.html', context=dict())


def redirect_original(request, short_id):
    url = get_object_or_404(Urls, pk=short_id)
    url.count += 1
    url.save()

    return HttpResponseRedirect(url.http_url)


def shorten_url(request):
    url = request.POST.get('url')

    if url is None:
        return HttpResponse(json.dumps({'error': 'error occurs'}))

    # генерируем короткий  URL
    short_url = get_short_url()

    db = Urls(short_id=short_url, http_url=url)
    db.save()

    response_data = dict(url=f'{settings.SITE_URL}/{short_url}')

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_short_url():
    length = 6  # длинна url
    char = f'{string.ascii_uppercase}{string.ascii_lowercase}{string.digits}'  # строка ASCI символов

    while True:
        short_url = ''.join(random.choice(char) for _ in range(length))

        if not Urls.check(pk=short_url): break

    return short_url
