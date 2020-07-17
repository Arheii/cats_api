from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
# from django.views.decorators.csrf import csrf_exempt

from . import views


router = routers.DefaultRouter()
router.register(r'cats', views.CatViewSet)
router.register(r'breeds', views.BreedViewSet)


urlpatterns = [
    # swagger for yaml
    path('', include(router.urls)),
    path('doc', TemplateView.as_view(
        template_name='rest/swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
     path('openapi/', get_schema_view(
        title="Cats",
        description="API via rest_framework and yaml generate"
    ), name='openapi-schema'),
    # api routes
    
]


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]