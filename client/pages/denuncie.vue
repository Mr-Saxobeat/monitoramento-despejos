<template>
  <div class="container mt-4 mb-5">
      <h1>Denunciar despejo:</h1>
    <b-form class="form-denuncia" @submit="onSubmit">
      <b-form-group
        label="Em qual município está ocorrendo a ação ou ameaças de despejo?"
        label-for="input_cidade"
      >
        <b-form-select
            id="input_cidade"
            v-model="form.cidade" 
            :options="cidades"
            required>
            <template #first>
              <b-form-select-option 
                :value="null" 
                disabled>
                  -- Selecione uma cidade --
                </b-form-select-option>
            </template>
        </b-form-select>
      </b-form-group>

      <b-form-group 
        label="Qual o nome da ocupação/comunidade onde ocorreu a ação ou ameaça de despejo?" 
        label-for="input_nome_ocupacao">
        <b-form-input
          id="input_nome_ocupacao"
          v-model="form.nome_ocupacao"
          placeholder="Nome da ocupação/comunidade"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group 
        label="Quantas famílias estão sendo despejadas ou ameaçadas?" 
        label-for="input_num_familias">
        <b-form-input
          type="number"
          id="input_num_familias"
          v-model="form.num_familias"
          placeholder="Digite o número de famílias"
          min=0
          value=0
          step=1
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group 
        label="Qual o endereço ou ponto de referência da ocupação ou comunidade que está sofrendo o despejo / ameaça de despejo?" 
        label-for="input_endereco">
        <b-form-input
          type="text"
          id="input_endereco"
          v-model="form.endereco"
          placeholder="Especifique da forma mais completa possível"
          required
        >
        </b-form-input>
      </b-form-group>

      <b-form-group 
        label="Estágio do conflito:" 
        label-for="input_situacao">
        <b-form-radio-group
          id="input_situacao"
          v-model="form.situacao"
          required
          stacked
          :options="capitalizeArray(['despejo já ocorreu', 'ameaça sem previsão de data'])"
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group 
        label="A ação ou ameaça de despejo ocorreu, está agendada ou tem grande risco de ocorrer durante a pandemia de Covid-19? (Março - período atual)" 
        label-for="input_pandemia">
        <b-form-radio-group
          id="input_pandemia"
          v-model="form.pandemia"
          required
          stacked
          :options="capitalizeArray(['sim', 'não'])"
        >
        </b-form-radio-group>
      </b-form-group>

      <b-form-group 
        label="Descreva o que aconteceu ou está acontecendo:" 
        label-for="input_descricao">
        <b-form-input
          type="text"
          id="input_descricao"
          v-model="form.descricao"
          placeholder="Descreva da forma mais completa possível"
          required
        >
        </b-form-input>
      </b-form-group>

      <b-form-group
        label="Como você classificaria a etnia (raça, cor) da maioria da comunidade?"
        label-for="input_etnia">
        <b-form-radio-group
          id="input_etnia"
          v-model="form.etnia"
          required
          stacked
          :options="capitalizeArray(['branca', 'preta', 'parda', 'amarela', 'indígena', 'outro'])">
        </b-form-radio-group>
      </b-form-group>

      <b-form-group
        label="Qual o gênero da MAIORIA dos líderes de família?"
        description="Cisgênero: é a pessoa que se identifica com o sexo biológico designado no momento de seu nascimento. Transgênero: é quem se identifica com um gênero diferente daquele atribuído no nascimento. Não-binário: é alguém que não se identifica completamente com o “gênero de nascença” nem com outro gênero. "
        label-for="input_genero">
        <b-form-radio-group
          id="input_genero"
          v-model="form.genero"
          required
          stacked
          :options="capitalizeArray(['homem cisgênero', 'mulher cisgênero', 'homem transgênero', 'mulher transgênero', 'não-binário', 'outro'])">
        </b-form-radio-group>
      </b-form-group>

      <b-form-group 
        label="Desde quando a comunidade/ocupação existe no local?"
        label-for="input_data_existencia">
        <b-form-datepicker
          id="input_data_existencia"
          v-model="form.data_existencia"
          placeholder="Caso não tenha uma data exata, o campo pode ser preenchido com o dia 1º do respectivo mês e ano."
          required
        ></b-form-datepicker>
      </b-form-group>

      <b-form-group 
        label="Desde quando existe a ameaça de despejo?"
        label-for="input_data_ameaca_despejo">
        <b-form-datepicker
          id="input_data_ameaca_despejo"
          v-model="form.data_ameaca_despejo"
          placeholder="Caso não tenha uma data exata, o campo pode ser preenchido com o dia 1º do respectivo mês e ano."
          required
        ></b-form-datepicker>
      </b-form-group>

      <b-form-group 
        label="Quando ocorreu ou para quando está agendado o despejo?"
        label-for="input_data_para_despejo">
        <b-form-datepicker
          id="input_data_para_despejo"
          v-model="form.data_para_despejo"
          placeholder="Caso não tenha uma data exata, o campo pode ser preenchido com o dia 1º do respectivo mês e ano."
          required
        ></b-form-datepicker>
      </b-form-group>

      <b-form-group 
        label="Qual o caráter do imóvel?"
        label-for="input_carater_imovel">
        <b-form-radio-group
          id="input_carater_imovel"
          v-model="form.carater_imovel"
          :options="capitalizeArray(['público', 'privado'])"
          required
          stacked
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group 
        label="Qual a tipologia da comunidade/ocupação?"
        label-for="input_tipologia">
        <b-form-radio-group
          id="input_tipologia"
          v-model="form.tipologia"
          :options="capitalizeArray(['ocupação de terreno', 'ocupação de edifício'])"
          required
          stacked
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group 
        label="Quem é responsável pela ameaça ou ação de despejo?"
        label-for="input_responsavel_despejo">
        <b-form-radio-group
          id="input_responsavel_despejo"
          v-model="form.responsavel"
          :options="capitalizeArray([
            'Proprietário privado', 
            'Município',
            'Governo do Estado',
            'Governo Federal',
            'Imobiliária',
            'Ministério Público',
            ])"
          required
          stacked
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group 
        label="Qual o motivo da ameaça de remoção ou despejo?"
        label-for="input_motivo">
        <b-form-radio-group
          id="input_motivo"
          v-model="form.motivo"
          :options="capitalizeArray([
            'reintegração de posse/conflito com o proprietário', 
            'impacto de obras públicas/projeto de urbanização',
            'não pagamento de parcela de aluguel',
            'não pagamento de parcela habitacional/rescisória de contrato',
            'área de risco',
            'questões ambientais/área de interesse ambiental',
            'outro'
            ])"
          required
          stacked
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group 
        label="Existe alguma ação na justiça? Informe o número se tiver conhecimento:" 
        label-for="input_cod_acao_justica">
        <b-form-input
          id="input_cod_acao_justica"
          v-model="form.cod_acao_justica"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group 
        label="Você tem algum link de notícia ou postagem sobre despejo?" 
        label-for="input_link_sobre_despejo">
        <b-form-input
          id="input_link_sobre_despejo"
          v-model="form.link_sobre_despejo"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group 
        label="A comunidade possui assessoria jurídica?"
        label-for="input_assessoria_juridica">
        <b-form-radio-group
          id="input_assessoria_juridica"
          v-model="form.assessoria_juridica"
          :options="capitalizeArray([
            'defensoria pública', 
            'ong',
            'coletivo',
            'advogado popular',
            'não',
            'outro'
            ])"
          required
          stacked
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group 
        label="Algum movimento social, entidade ou coletivo já estão acompanhando o caso? Se sim, qual?"
        label-for="input_movimento_social">
        <b-form-radio-group
          id="input_movimento_social"
          v-model="form.movimento_social"
          :options="capitalizeArray([
            'MNLM (Movimento Nacional de Luta por Moradia)', 
            'Brigadas Populares',
            'MST (Movimento dos Sem Terra)',
            'não',
            'outro'
            ])"
          required
          stacked
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group 
        label="Houve ameaça a alguma liderança comunitária por causa da ameaça de despejo ou do despejo? Se sim, explique." 
        label-for="input_ameaca_a_lideranca">
        <b-form-input
          id="input_ameaca_a_lideranca"
          v-model="form.ameaca_a_lideranca"
          placeholder="Descreva de forma mais completa possível"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group 
        label="Se possível, informe uma pessoa e telefone com DDD para contato (caso precisarmos complementar alguma informação sobre o caso)." 
        label-for="input_contato">
        <b-form-input
          id="input_contato"
          v-model="form.contato"
          required
        ></b-form-input>
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

        // cidades.push({value: null, text: "Selecione uma cidade"})
        json_cidades.features.forEach(cidade => {
          cidades.push({value: cidade.properties.nome, text: cidade.properties.nome})
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
          etnia: null,
          data_existencia: null,
          data_ameaca_despejo: null,
          data_para_despejo: null,
          carater_imovel: null,
          tipologia: null,
          responsavel: null,
          motivo: null,
          cod_acao_justica: null,
          link_sobre_despejo: null,
          assessoria_juridica: null,
          movimento_social: null,
          ameaca_a_lideranca: null,
          contato: null,
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

<style>
.form-denuncia > .form-group {
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 2px dotted rgba(150, 150, 150);
}
</style>