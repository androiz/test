import coreapi
from filer.models import File as FilerFile
from django.core.files import File as File
from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator

from .models import Prueba, Nested


class PruebaSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Prueba
        fields = '__all__'


class PruebaViewSet(viewsets.ModelViewSet):
    """
    description:
    La entidad prueba
    
    ### retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.
    """
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

    @list_route(methods=['post', 'put'])
    def testMethod(self, request):
        """
        Returns a 202.
        """
        return Response()

    def create(self, request, *args, **kwargs):
        """
        Return a list of all the existing users.
        """
        filename = request.FILES['file']._name
        filepath = request.FILES['file'].file.name
        # user = User.objects.get(username='testuser')
        with open(filepath, "rb") as f:
            file_obj = File(f, name=filename)
            file = FilerFile.objects.create(
                # owner=user,
                original_filename=filename,
                file=file_obj
            )
        p = Prueba.objects.create(
            file=file
        )
        serializer = PruebaSerializer(p)
        if p:
            return Response(serializer.data)
        else:
            p.delete()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prueba
        fields = '__all__'


class NestedViewSet(viewsets.ModelViewSet):
    queryset = Nested.objects.all()
    serializer_class = NestedSerializer


