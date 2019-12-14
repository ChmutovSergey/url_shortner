import json
import random
import string
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from hashlib import md5

from .models import Urls


def index(request):
    data = dict()

    return render(request, 'shortenersite/index.html', context=data)


def redirect_original(request, md_url):
    url = get_object_or_404(Urls, pk=md_url)

    return HttpResponseRedirect(url.http_url)


def shorten_url(request):
    url = request.POST.get('url')

    if url is None:
        return HttpResponse(json.dumps({'error': 'error occurs'}))

    # проверяем есть ли такой урл уже в БД
    md5_url = get_md5_hash(url)
    # генерируем короткий  URL
    short_url = get_short_url()


def get_md5_hash(url: str) -> str:
    hash_obj = md5(url.encode('utf-8'))

    return hash_obj.hexdigest()


def get_short_url():
    length = 6  # длинна url
    char = f'{string.ascii_uppercase}{string.ascii_lowercase}{string.digits}'  # строка ASCI символов

    short_url = ''.join(random.choice(char) for _ in range(length))
    # TODO: реализовать проверку на уникальность короткого URL

    return short_url
