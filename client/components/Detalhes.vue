<template>
    <div>
        <l-control :position=this.position>
            <b-card
                title="Detalhes:"
                tag="article"
                style="max-width: 20rem;"
                class="leaflet-touch leaflet-control-layers"
            >
                <b-card-text>
                    <div v-if="despejo">
                        <ul>
                            <li><strong>Cidade:</strong> {{ despejo.properties.cidade }}</li>
                            <li><strong>Ocupação:</strong> {{ despejo.properties.nome_ocupacao }}</li>
                            <li><strong>Número de famílias:</strong> {{ despejo.properties.num_familias }}</li>
                        </ul>
                    </div>
                    <div v-else>
                        <p>Selecione algum despejo.</p>
                    </div>
                </b-card-text>
            </b-card>
        </l-control>
    </div>
</template>

<script>
export default {
    props: ["position", "despejo", "despejo"],
}
</script>

<style scoped>
ul {
    text-align: left;
    padding-left: 20px;
}
</style>