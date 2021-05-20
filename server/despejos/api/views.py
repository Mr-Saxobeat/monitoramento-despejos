from rest_framework.views import APIView
from rest_framework import generics, pagination
from rest_framework.views import Response
from djgeojson.views import GeoJSONLayerView
from despejos.models import Despejo, Cidade, LayerDefinition
from despejos.api.serializers import DespejoSerializer, CidadeSerializer, LayerDefinitionSerializer
from django.contrib.gis.geos import Point
from rest_framework import status, viewsets
import datetime
from django.core.exceptions import ObjectDoesNotExist


class LayerDefinitionView(generics.ListAPIView):
    queryset = LayerDefinition.objects.all()
    serializer_class = LayerDefinitionSerializer


class CidadeListView(generics.ListAPIView):
    queryset = Cidade.objects.all().order_by('nome')
    serializer_class = CidadeSerializer
    # pagination_class = pagination.PageNumberPagination
    # page_size = 10


class DespejoViewSet(viewsets.ViewSet):
    serializer_class = DespejoSerializer

    def get_queryset(self):
        return Despejo.objects.filter(geom__isnull=False)

    def list(self, request):
        return Response(self.serializer_class(self.get_queryset(), many=True).data,
                        status=status.HTTP_200_OK)

    def create(self, request):
        latitude = request.data.get('latitude', None)
        longitude = request.data.get('longitude', None)
        nome_cidade = request.data.get('cidade', None)
        data_existencia = request.data.get('data_existencia', None)
        data_ameaca_despejo = request.data.get('data_ameaca_despejo', None)
        data_para_despejo = request.data.get('data_para_despejo', None)

        if data_existencia == "":
            data_existencia = datetime.date(1, 1, 1)
        else:
            # data_existencia = datetime.datetime.strptime(data_existencia, '%d/%m/%Y').date()
            data_existencia = datetime.datetime.strptime(data_existencia, '%Y-%m-%d').date()

        if data_ameaca_despejo == "":
            data_ameaca_despejo = datetime.date(1, 1, 1)
        else:
            data_ameaca_despejo = datetime.datetime.strptime(data_ameaca_despejo, '%Y-%m-%d').date()

        if data_para_despejo == "":
            data_para_despejo = datetime.date(1, 1, 1)
        else:
            data_para_despejo = datetime.datetime.strptime(data_para_despejo, '%Y-%m-%d').date()

        if latitude == None or longitude == None:
            point = None
        else:
            point = Point(float(longitude), float(latitude))

        try:
            cidade = Cidade.objects.get(nome=nome_cidade)
        except ObjectDoesNotExist:
            return Response(data={
                                'message': 'O município fornecido não é válido.'
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(
                geom=point, 
                cidade=cidade,
                data_existencia=data_existencia,
                data_ameaca_despejo=data_ameaca_despejo,
                data_para_despejo=data_para_despejo,
                )
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)