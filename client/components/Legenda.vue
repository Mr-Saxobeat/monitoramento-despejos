<template>
    <div>
        <l-control
        class="legend-control"
        :position=this.position
        >
            <b-card
                title="Legenda:"
                tag="article"
                style="max-width: 20rem;"
                class="leaflet-touch leaflet-control-layers"
            >
                <b-card-text>
                    <ul>
                        <li 
                        v-for="legenda in layer_definition.legendas" 
                        :key="legenda.descricao">
                            <span
                            v-bind:style="{ backgroundColor: legenda.cod_cor,}"
                            class="list-dot"
                            ></span>
                            {{ legenda.descricao | capitalize }}
                        </li>
                    </ul>
                </b-card-text>
            </b-card>
        </l-control>
    </div>
</template>

<script>
export default {
    props: ["position", "layer_definition"],
    filters: {
    capitalize: function (value) {
            if (!value) return ''
            value = value.toString()
            return value.charAt(0).toUpperCase() + value.slice(1)
        }
    }
}
</script>

<style scoped>
h1{
    margin: 0;
    padding: 0;
}

ul{
    margin: 0;
    list-style-type: none;
    padding-left: 10px;
    text-align: left;
}

.list-dot {
    border: 2px solid black;
    margin: 0;
    height: 15px;
    width: 15px;
    border-radius: 50%;
    display: inline-block;
}
</style>