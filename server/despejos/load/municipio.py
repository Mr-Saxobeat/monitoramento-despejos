import os
from django.contrib.gis.utils import LayerMapping
from despejos.models import Cidade

cidade_mapping = {
    'fid': 'FID',
    'nome': 'nome',
    'geom': 'POLYGON',
}

shp_file = os.path.join(os.getcwd(), 'dados', 'municipios_es', 'simply', 'ES_Municipios.shp')

def run(verbose=True):
    lm = LayerMapping(Cidade, shp_file, cidade_mapping)
    lm.save(strict=True, verbose=verbose)
