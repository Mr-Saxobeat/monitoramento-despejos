from django.contrib.gis import admin
from despejos.models import Despejo, LayerDefinition, Legenda, Cor

class DespejoAdmin(admin.GeoModelAdmin):
    list_display = ('nome_ocupacao', 'cidade')


admin.site.register(Despejo, DespejoAdmin)
admin.site.register(LayerDefinition)
admin.site.register(Legenda)
admin.site.register(Cor)
