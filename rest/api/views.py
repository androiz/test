import json
import os

from django.http import HttpResponse

from config.settings import BASE_DIR


def swagger_json(request):
    path = os.path.join(BASE_DIR, 'static', 'swagger.json')
    with open(path, 'r') as myfile:
        data = myfile.read()
    response = HttpResponse(content=data)
    response['Content-Type'] = 'application/json'
    return response
