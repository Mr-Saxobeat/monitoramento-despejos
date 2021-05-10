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
                            <!-- <li><strong>Endereço:</strong> {{ despejo.properties.endereco }}</li> -->
                            <!-- <li><strong>Descrição:</strong> {{ despejo.properties.descricao }}</li> -->
                            <li><strong>Data de existência:</strong> {{ despejo.properties.data_existencia }}</li>
                            <li><strong>Data de ameaça de despejo:</strong> {{ despejo.properties.data_ameaca_despejo }}</li>
                            <li><strong>Data marcada para o despejo:</strong> {{ despejo.properties.data_para_despejo }}</li>
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
    props: ["position", "despejo"],
}
</script>

<style scoped>
ul {
    text-align: left;
    padding-left: 20px;
}
</style>