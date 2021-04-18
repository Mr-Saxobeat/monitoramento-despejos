from django.urls import include, path
from . import views as v

app_name = 'despejos'

urlpatterns = [
    path('api/', include('despejos.api.urls')),
    path('', v.IndexView)
]