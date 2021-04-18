from django.urls import path
from despejos.api import views as v


urlpatterns = [
    path('despejo/', v.DespejoAPIView.as_view(), name='despejo-list'),
    path('cidade/', v.CidadeListView.as_view(), name='cidade-list'),
    path('layerdefinition/', v.LayerDefinitionView.as_view(), name='layer-definition-list'),
]