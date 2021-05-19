<template>
  <div class="container mt-4 mb-5">
      <h1>Denunciar despejo:</h1>
    <b-form @submit="onSubmit">
      <b-form-group
        id="input-group-1"
        label="Em qual município está ocorrendo a ação ou ameaças de despejo?"
        label-for="input_cidade"
        description=""
      >
        <b-form-select
            id="input_cidade"
            type="select"
            placeholder="Selecione a cidade"
            v-model="form.cidade" 
            :options="cidades"
            required
        ></b-form-select>
      </b-form-group>

      <b-form-group 
        id="input-group-2" 
        label="Qual o nome da ocupação/comunidade onde ocorreu a ação ou ameaça de despejo?" 
        label-for="input_nome_ocupacao">
        <b-form-input
          id="input-nome-da-ocupacao"
          v-model="form.nome_ocupacao"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group 
        id="input-group-3" 
        label="Quantas famílias estão sendo despejadas ou ameaçadas?" 
        label-for="input_num_familias">
        <b-form-input
          type="number"
          id="input_num_familias"
          v-model="form.num_familias"
          min=0
          value=0
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group 
        id="input-group-4" 
        label="Qual o endereço ou ponto de referência da ocupação ou comunidade que está sofrendo o despejo / ameaça de despejo? (especificar da forma mais completa possível) " 
        label-for="input_endereço">
        <b-form-input
          type="text"
          id="input_endereco"
          v-model="form.endereco"
          required
        >
        </b-form-input>
      </b-form-group>

      <b-form-group 
        id="input-group-5" 
        label="Estágio do conflito:" 
        label-for="input_situacao">
        <b-form-select
          id="input_situacao"
          v-model="form.situacao"
          required
          :options="capitalizeArray(['despejo já ocorreu', 'ameaça sem previsão de data'])"
        >
        </b-form-select>
      </b-form-group>

      <b-form-group 
        id="input-group-6" 
        label="A ação ou ameaça de despejo ocorreu, está agendada ou tem grande risco de ocorrer durante a pandemia de Covid-19? (Março - período atual)" 
        label-for="input_pandemia">
        <b-form-select
          id="input_pandemia"
          v-model="form.pandemia"
          required
          :options="capitalizeArray(['sim', 'não'])"
        >
        </b-form-select>
      </b-form-group>

      <b-form-group 
        id="input-group-7" 
        label="Descreva o que aconteceu ou está acontecendo:" 
        label-for="input_descricao">
        <b-form-input
          type="text"
          id="input_descricao"
          v-model="form.descricao"
          required
        >
        </b-form-input>
      </b-form-group>

      <b-form-group 
        id="input-group-8" 
        label="Desde quando a comunidade/ocupação existe no local?"
        description="Caso não tenha uma data exata, o campo pode ser preenchido com o dia 1º do respectivo mês e ano."
        label-for="input_data_existencia">
        <b-form-datepicker
          id="input_data_existencia"
          v-model="form.data_existencia"
          required
        >
        </b-form-datepicker>
      </b-form-group>

      <b-form-group 
        id="input-group-9" 
        label="Desde quando existe a ameaça de despejo?"
        description="Caso não tenha uma data exata, o campo pode ser preenchido com o dia 1º do respectivo mês e ano."
        label-for="input_data_ameaca_despejo">
        <b-form-datepicker
          id="input_data_ameaca_despejo"
          v-model="form.data_ameaca_despejo"
          required
        >
        </b-form-datepicker>
      </b-form-group>

      <b-form-group 
        id="input-group-10" 
        label="Quando ocorreu ou para quando está agendado o despejo?"
        description="Caso não tenha uma data exata, o campo pode ser preenchido com o dia 1º do respectivo mês e ano."
        label-for="input_data_para_despejo">
        <b-form-datepicker
          id="input_data_para_despejo"
          v-model="form.data_para_despejo"
          required
        >
        </b-form-datepicker>
      </b-form-group>

      <b-form-group 
        id="input-group-11" 
        label="Qual o caráter do imóvel?"
        label-for="input_carater_imovel">
        <b-form-select
          id="input_carater_imovel"
          v-model="form.carater_imovel"
          :options="capitalizeArray(['público', 'privado'])"
          required
        >
        </b-form-select>
      </b-form-group>

      <b-form-group 
        id="input-group-12" 
        label="Qual a tipologia da comunidade/ocupação? "
        label-for="input_tipologia">
        <b-form-select
          id="input_tipologia"
          v-model="form.tipologia"
          :options="capitalizeArray(['ocupação de terreno', 'ocupação de edifício'])"
          required
        >
        </b-form-select>
      </b-form-group>

      <b-form-group 
        id="input-group-13"
        label="Quem é responsável pela ameaça ou ação de despejo?"
        label-for="input_responsavel_despejo">
        <b-form-select
          id="input_responsavel_despejo"
          v-model="form.responsavel_despejo"
          :options="capitalizeArray([
            'Proprietário privado', 
            'Município',
            'Governo do Estado',
            'Governo Federal',
            'Imobiliária',
            'Ministério Público',
            ])"
          required
        >
        </b-form-select>
      </b-form-group>

      <b-button type="submit" variant="primary">Enviar denúncia</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    async asyncData({ $axios, params }) {
      try{
        let json_cidades = await $axios.$get('cidade/')
        let cidades = []

        json_cidades.features.forEach(cidade => {
          cidades.push(cidade.properties.nome)
        });

        return { cidades }
      } catch(e) {
        console.log(e)
        return []
      }
    },
    data() {
      return {
        form: {
          cidade: null,
          nome_ocupacao: null,
          num_familias: null,
          endereco: null,
          situacao: null,
          pandemia: null,
          descricao: null,
          data_existencia: null,
          data_ameaca_despejo: null,
          data_para_despejo: null,
          carater_imovel: null,
          tipologia: null,
          responsavel_despejo: null
        },
      }
    },
    methods: {
      async onSubmit(event) {
        event.preventDefault()
        let response = await this.$axios.post('despejo/', this.form)
        window.location.reload()
      },
      capitalizeArray(array_str) {
        let capitalizedArray = []

        array_str.forEach(oneString => {
          capitalizedArray.push(oneString[0].toUpperCase() + oneString.slice(1))
        })

        return capitalizedArray
      }
    },
  }
</script>