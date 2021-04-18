<template>
    <div>
        <l-control
             :position=this.position
            >
            <div class="info-control">
                <div v-if="despejo">
                    <h3>Detalhes:</h3>
                    <ul>
                        <li><strong>Cidade:</strong> {{ despejo.properties.cidade }}</li>
                        <li><strong>Ocupação:</strong> {{ despejo.properties.nome_ocupacao }}</li>
                        <li><strong>Número de famílias:</strong> {{ despejo.properties.num_familias }}</li>
                    </ul>
                </div>
                <div v-else>
                    <h3>Selecione algum despejo.</h3>
                </div>
            </div>
        </l-control>
    </div>
</template>

<script>
export default {
    props: ["position", "despejo"],
}
</script>

<style scoped>
.info-control {
    padding: 0;
    margin: 0;
    border: 2px solid black;
    border-radius: 5px;
    background-color: #ffffff;
    /* height: 100px; */
    width: 200px;
    align-content: left;
}

ul {
    text-align: left;
    padding-left: 20px;
}
</style>