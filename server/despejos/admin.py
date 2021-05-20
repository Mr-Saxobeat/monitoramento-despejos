from despejos.forms import DespejoForm
from django.contrib.gis import admin
from despejos.models import Despejo, LayerDefinition, Legenda, Cor

@admin.register(Despejo)
class DespejoAdmin(admin.ModelAdmin):
    list_display = ('nome_ocupacao', 'cidade', 'num_familias', 'geom')
    form = DespejoForm


admin.site.register(LayerDefinition)
admin.site.register(Legenda)
admin.site.register(Cor)
