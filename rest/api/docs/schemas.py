import coreapi
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


"""
action:
    get, post, delete, put, patch
location: 
    form, path, query, body*
type: 
    integer, string, float, date
"""

TRAVEL = {
    'travel': {
        'list': coreapi.Link(
            url='/travel/',
            action='get',
            fields=[
                coreapi.Field(
                    name='st',
                    required=False,
                    location='query',
                    description='Estado del viaje',
                    type='string'
                ),
                coreapi.Field(
                    name='str',
                    required=True,
                    location='form',
                    description='City name or airport code.'
                )
            ],
            description='Return flight availability and prices.'
        ),
        'create': coreapi.Link(
            url='/travel/{pk}/',
            action='post',
            fields=[
                coreapi.Field(
                    name='pk',
                    required=True,
                    location='path',
                    description='City name or airport code.'
                )
            ],
            description='Return flight availability and prices.'
        ),
    }
}


DESTINATION = {
    'destination': {
        'list': coreapi.Link(
            url='/travel/{pk}/destination/',
            action='get',
            fields=[
                coreapi.Field(
                    name='pk',
                    required=True,
                    location='path',
                    description='City name or airport code.'
                ),
                coreapi.Field(
                    name='to',
                    required=True,
                    location='query',
                    description='City name or airport code.'
                ),
                coreapi.Field(
                    name='date',
                    required=True,
                    location='query',
                    description='Flight date in "YYYY-MM-DD" format.'
                )
            ],
            description='Return flight availability and prices.'
        ),
        'create': coreapi.Link(
            url='/travel/{pk}/destination/',
            action='post',
            fields=[
                coreapi.Field(
                    name='pk',
                    required=True,
                    location='path',
                    description='City name or airport code.'
                ),
                coreapi.Field(
                    name='date',
                    required=True,
                    location='form',
                    type='number',
                    example='88687',
                    description='Fecha en timestamp'
                ),
                coreapi.Field(
                    name='destinos',
                    required=True,
                    location='form',
                    description='City name or airport code.',
                    type={
                        "$ref": "Menu"
                    }
                )
            ],
            description='Return flight availability and prices.'
        ),
    }
}

content = {**TRAVEL, **DESTINATION}

schema = coreapi.Document(
    title='Flight Search API',
    url='https://api.example.org/',
    content=content
)


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    return Response(schema)
