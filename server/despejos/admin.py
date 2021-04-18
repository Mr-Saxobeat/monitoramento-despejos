from django.contrib.gis import admin
from despejos.models import Despejo, LayerDefinition, Legenda, Cor

admin.site.register(Despejo, admin.GeoModelAdmin)
admin.site.register(LayerDefinition)
admin.site.register(Legenda)
admin.site.register(Cor)
