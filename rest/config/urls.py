from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from api.rest import PruebaViewSet
from api.docs import schemas
from api import views

router = DefaultRouter()
router.register(r'prueba/(?P<id>[0-9]+)/nested', PruebaViewSet, base_name='nested')
router.register(r'prueba', PruebaViewSet, base_name='prueba')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url('^swagger.json$', views.swagger_json),
    url('^docs$', schemas.schema_view),
]
