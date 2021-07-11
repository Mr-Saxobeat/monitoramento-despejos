<template>
    <div>
        <l-control :position=this.position>
            <b-card
                title="Detalhes:"
                tag="article"
                style="max-width: 20rem;"
                class="leaflet-touch leaflet-control-layers"
            >
                <b-card-text class="detalhes-content">
                    <div v-if="despejo">
                        <ul>
                            <li>Cidade: {{ despejo.properties.cidade }}</li>
                            <li>Ocupação: {{ despejo.properties.nome_ocupacao }}</li>
                            <li>Número de famílias: {{ despejo.properties.num_familias }}</li>
                            <li>Endereço: {{ despejo.properties.endereco }}</li>
                            <li>Descrição: {{ despejo.properties.descricao }}</li>
                            <li v-if="data_existencia.ano > 1">Data de existência: {{ data_existencia.data }}</li>
                            <li v-if="data_ameaca_despejo.ano > 1">Data de ameaça de despejo: {{ data_ameaca_despejo.data }}</li>
                            <li v-if="data_para_despejo.ano > 1">Data marcada para o despejo: {{ data_para_despejo.data }}</li>
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
    computed: {
        data_existencia() {
            let data = this.despejo.properties.data_existencia
            let ano = parseInt(data.slice(0, 4))
            let mes = parseInt(data.slice(5, 7))
            let dia = parseInt(data.slice(8))

            return {ano: ano, mes: mes, dia: dia, data: dia + "/" + mes + "/" + ano}
        },

        data_ameaca_despejo() {
            let data = this.despejo.properties.data_ameaca_despejo
            let ano = parseInt(data.slice(0, 4))
            let mes = parseInt(data.slice(5, 7))
            let dia = parseInt(data.slice(8))

            return {ano: ano, mes: mes, dia: dia, data: dia + "/" + mes + "/" + ano}
        },

        data_para_despejo() {
            let data = this.despejo.properties.data_para_despejo
            let ano = parseInt(data.slice(0, 4))
            let mes = parseInt(data.slice(5, 7))
            let dia = parseInt(data.slice(8))

            return {
                ano: ano,
                mes: mes,
                dia: dia,
                data: dia + "/" + mes + "/" + ano
            }
        },
    },
}
</script>

<style scoped>
.detalhes-content{
    padding: 0;
    height: 230px;
    overflow-x: hidden;
    overflow-y: auto;
}

ul {
    text-align: left;
    padding-left: 20px;
    list-style: none;
}
</style>
