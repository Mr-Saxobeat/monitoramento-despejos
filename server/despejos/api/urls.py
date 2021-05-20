from django.urls import path
from despejos.api import views as v
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'despejo', v.DespejoViewSet, basename='despejo')
urlpatterns = router.urls

urlpatterns += [
    path('cidade/', v.CidadeListView.as_view(), name='cidade-list'),
    path('layerdefinition/', v.LayerDefinitionView.as_view(), name='layer-definition-list'),
]