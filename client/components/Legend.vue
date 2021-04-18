<template>
    <div>
        <l-control
        class="legend-control"
        :position=this.position
        >
            <h1>Legenda:</h1>
            <ul>
                <li 
                v-for="legenda in layer_definition.legendas" 
                :key="legenda.descricao">
                    <span
                    v-bind:style="{ backgroundColor: legenda.cod_cor,}"
                    class="list-dot"
                    ></span>
                    {{ legenda.descricao }}
                </li>
            </ul>
        </l-control>
    </div>
</template>

<script>
export default {
    props: ["position", "layer_definition"]
}
</script>

<style scoped>
h1{
    margin: 0;
    padding: 0;
}

.legend-control{
    padding: 0;
    margin: 0;
    border: 2px solid black;
    border-radius: 5px;
    background-color: #ffffff;
    height: 100px;
    width: 200px;
    align-content: left;
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