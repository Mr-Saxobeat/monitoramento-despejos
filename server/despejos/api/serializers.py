from despejos.models import Despejo, Cidade, LayerDefinition, Legenda
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class CidadeSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Cidade
        fields = '__all__'
        geo_field = 'geom'


class DespejoSerializer(GeoFeatureModelSerializer):
    cidade = serializers.StringRelatedField()
    popup_content = serializers.StringRelatedField()

    class Meta:
        model = Despejo
        fields = '__all__'
        geo_field = 'geom'


class LegendaSerializer(serializers.ModelSerializer):
    cor = serializers.SerializerMethodField()

    class Meta:
        model = Legenda
        fields = '__all__'

    def get_cor(self, obj):
        return cor.cod

class LayerDefinitionSerializer(serializers.ModelSerializer):
    legendas = serializers.SerializerMethodField()

    class Meta:
        model = LayerDefinition
        fields = '__all__'

    def get_legendas(self, obj):
        return [
            {
                'descricao': leg.descricao,
                'cod_cor': leg.cor.cod
            }

            for leg in obj.legendas.all()
        ]