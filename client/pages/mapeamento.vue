<template>
    <div id="map-wrap" class="container-fluid">
        <l-map
            style="height: 100%; width: 100%"
            :zoom="zoom"
            :center="center"
            v-on:baselayerchange="baselayerchanged"
        >
            <l-tile-layer :url="url"></l-tile-layer>

            <l-geo-json 
                :geojson="city_geojson" 
            ></l-geo-json>

            <l-control-layers
                position="bottomright"
                :collapsed="false"
            ></l-control-layers>

            <div v-if="despejos_geojson">
                <l-layer-group
                v-for="layer_opts in layers_definitions"
                :key="layer_opts.id + 200"
                :name="layer_opts.nome_visualizacao"
                :visible="true"
                layerType="base"
            >
                <l-circle-marker
                    v-for="despejo in despejos_geojson.features"
                    :lat-lng="[despejo.geometry.coordinates[1], despejo.geometry.coordinates[0]]"
                    :key="despejo.id + 100"
                    :weigth="5"
                    :radius="10"
                    :color="getCircleColor(despejo, layer_opts)"
                    :fillColor="getCircleColor(despejo, layer_opts)"
                    @click="onCircleMarkerClick($event, despejo)"
                ></l-circle-marker>
            </l-layer-group>

            <Legenda
                position="bottomright"
                :layer_definition="active_layer"
            />

            <Detalhes 
                position="bottomright"
                :despejo="selectedDespejo" 
            />
            </div>
            
        </l-map>
    </div>
</template>

<script>
export default {
    async asyncData({ $axios, params }) {
      try {
        let city_geojson = await $axios.$get('cidade/')
        let despejos_geojson = await $axios.$get('despejo/')
        let layers_definitions = await $axios.$get('layerdefinition/')
        return { city_geojson, despejos_geojson, layers_definitions }
      } catch(e) {
        return []
      }
    },
    data() {
        return {
            visibleLayer: true,
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            apiBaseUrl: 'http://127.0.0.1:8000/',
            zoom: 7,
            center: [-19.178876, -39.484863],
      
            active_layer: {},
            city_layer_options: {
                style: {
                    color: 'black',
                    weight: 2,
                    opacity: 0.1,
                },
            },
            selectedDespejo: null,
            classeteste: "info-mapa",
        }
    },

    methods: {
        // zoomUpdated(zoom) {
        //     console.log("Zoom " + zoom)
        // },
        // centerUpdated(center) {
        //     console.log("Centro " + center)
        // },
        getVisibleLayer() {
            if(this.visibleLayer == true) {
                this.visibleLayer = false;
                return true;
            } else {
                console.log(false);
                return false;
            }
        },
        onCircleMarkerClick(event, despejo) {
            this.selectedDespejo = despejo;
        },
        getCircleColor(despejo, layer_opts) {
            var color = null;
            var value = despejo.properties[layer_opts.nome] == null ? "" : despejo.properties[layer_opts.nome].toLowerCase();
            switch (layer_opts.nome){
                case "situacao":
                    color = value === layer_opts.legendas[0].descricao ? layer_opts.legendas[0].cod_cor : layer_opts.legendas[1].cod_cor;
                    break;
                case "tipologia":
                    color = value === layer_opts.legendas[0].descricao ? layer_opts.legendas[0].cod_cor : layer_opts.legendas[1].cod_cor;
                    break;
                case "carater_imovel":
                    color = value === layer_opts.legendas[0].descricao ? layer_opts.legendas[0].cod_cor : layer_opts.legendas[1].cod_cor;
                    break;
                case "zona":
                    color = value === layer_opts.legendas[0].descricao ? layer_opts.legendas[0].cod_cor : layer_opts.legendas[1].cod_cor;
                    break;
                case "pandemia":
                    color = value === layer_opts.legendas[0].descricao ? layer_opts.legendas[0].cod_cor : layer_opts.legendas[1].cod_cor;
                    break;
            }

            return color;
        },
        baselayerchanged: function(layer) {
            this.layers_definitions.forEach(l => {
                if(l.nome_visualizacao == layer.name) {
                    this.active_layer = l;
                }
            }); 
        },
    },
}
</script>

<style>
.leaflet-right > .leaflet-control{
    width: 600px;
    margin: 0;
    align-items: center;
}

.leaflet-right > .leaflet-control > .card {
    max-width: 100% !important;
}

.leaflet-control-layers{
    font-family: 'Saira', sans-serif;
}

.leaflet-control-layers li, .leaflet-control-layers span {
    font-size: 20px;
}
</style>