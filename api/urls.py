from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('<str:req>', views.Query_broker_View.as_view(), name='query_broker'),
    path('info/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'info/docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema'
        ),
        name='swagger-ui',
    ),
]