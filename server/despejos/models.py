from django.contrib.gis.db import models

class Cidade(models.Model):
    fid = models.BigIntegerField()
    nome = models.CharField(max_length=50)
    geom = models.PolygonField(srid=4326)

    def __str__(self):
        return self.nome


class Despejo(models.Model):
    geom = models.PointField(null=True, blank=True)
    cidade = models.ForeignKey(
                    to=Cidade, 
                    verbose_name='cidade', 
                    on_delete=models.CASCADE, 
                    related_name='despejos',
                    blank=True,
                    null=True,
                )
    nome_ocupacao = models.CharField('nome da ocupação', max_length=200, blank=True, null=True)
    num_familias = models.CharField(max_length=200, blank=True, null=True)
    endereco = models.CharField('endereço da ocupação', max_length=600, blank=True, null=True)
    situacao = models.CharField('situação', max_length=100, blank=True, null=True)
    pandemia = models.CharField('despejo durante a pandemia', max_length=10, blank=True, null=True)
    descricao = models.TextField('descrição do despejo', blank=True, null=True)
    etnia = models.CharField('etnia', max_length=100, blank=True, null=True)
    data_existencia = models.DateField('data de existência da ocupação', blank=True, null=True)
    data_ameaca_despejo = models.DateField('data de ameaça do despejo', blank=True, null=True)
    data_para_despejo = models.DateField('data marcada para o despejo', blank=True, null=True)
    carater_imovel = models.CharField('caráter do imóvel', max_length=100, blank=True, null=True)
    tipologia = models.CharField('tipologia', max_length=100, blank=True, null=True)
    zona = models.CharField('zona', max_length=100, blank=True, null=True)
    responsavel = models.CharField('responsável pelo despejo', max_length=100, blank=True, null=True)
    motivo = models.CharField('motivo para o despejo', max_length=500, blank=True, null=True)
    cod_acao_justica = models.CharField('código da ação na justica', max_length=100, blank=True, null=True)
    link_sobre_despejo = models.CharField('link sobre o despejo', max_length=500, blank=True, null=True)
    assessoria_juridica = models.CharField('assessoria jurídica', max_length=200, blank=True, null=True)
    movimento_social = models.CharField('movimento social', max_length=200, blank=True, null=True)
    ameaca_a_lideranca = models.TextField('ameaça a liderança', blank=True, null=True)

    @property
    def latitude(self):
        return self.geom.y

    @property
    def longitude(self):
        return self.geom.x

    @property
    def popup_content(self):
        popup_content = '<span><strong>Nome da ocupação: </strong></span>{}<br>'.format(self.nome_ocupacao)
        popup_content += '<span><strong>Nº de famílias: </strong></span>{}<br>'.format(self.num_familias)
        popup_content += '<span><strong>Endereço: </strong></span>{}<br>'.format(self.endereco)
        popup_content += '<span><strong>Situação: </strong></span>{}<br>'.format(self.situacao)
        popup_content += '<span><strong>Despejo durante a pandemia: </strong></span>{}<br>'.format(self.pandemia)
        popup_content += '<span><strong>Data de existência da ocupação: </strong></span>{}<br>'.format(self.data_existencia.strftime('%d/%m/%Y'))
        popup_content += '<span><strong>Data de ameaça do despejo: </strong></span>{}<br>'.format(self.data_ameaca_despejo.strftime('%d/%m/%Y'))
        popup_content += '<span><strong>Data para o despejo: </strong></span>{}<br>'.format(self.data_para_despejo.strftime('%d/%m/%Y'))
        popup_content += '<span><strong>Tipologia: </strong></span>{}<br>'.format(self.tipologia)
        popup_content += '<span><strong>Caráter do imóvel: </strong></span>{}<br>'.format(self.carater_imovel)
        popup_content += '<span><strong>Zona: </strong></span>{}<br>'.format(self.zona)

        return popup_content

    def __str__(self):
        return self.cidade.nome


class Cor(models.Model):
    nome = models.CharField(max_length=100)
    cod = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Legenda(models.Model):
    descricao = models.CharField(max_length=100)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class LayerDefinition(models.Model):
    nome_visualizacao = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    legendas = models.ManyToManyField(Legenda)

    def __str__(self):
        return self.nome_visualizacao