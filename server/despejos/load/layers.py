from despejos.models import LayerDefinition, Cor, Legenda

def run():
    cor, created = Cor.objects.get_or_create(
        nome='vermelho-0',
        cod='#fc0303'
    )

    leg1, created = Legenda.objects.get_or_create(
        descricao='despejo já ocorreu',
        cor=cor
    )

    cor, created = Cor.objects.get_or_create(
        nome='azul-0',
        cod='#030bfc'
    )

    leg2, created = Legenda.objects.get_or_create(
        descricao='ameaça sem previsão de data',
        cor=cor
    )

    ld, created = LayerDefinition.objects.get_or_create(
        nome='situacao',
        nome_visualizacao='Situação',
    )

    ld.legendas.add(leg1, leg2)
    ld.save()

    ###############################################

    cor, created = Cor.objects.get_or_create(
        nome='laranja-0',
        cod='#ff9d00'
    )

    leg1, created = Legenda.objects.get_or_create(
        descricao='ocupação de terreno',
        cor=cor
    )

    cor, created = Cor.objects.get_or_create(
        nome='cinza-0',
        cod='#6b6a69'
    )

    leg2, created = Legenda.objects.get_or_create(
        descricao='ocupação de edifício',
        cor=cor
    )

    ld, created = LayerDefinition.objects.get_or_create(
        nome='tipologia',
        nome_visualizacao='Tipologia',
    )

    ld.legendas.add(leg1, leg2)
    ld.save()

    ###############################################

    cor, created = Cor.objects.get_or_create(
        nome='verde-0',
        cod='#00bd06'
    )

    leg1, created = Legenda.objects.get_or_create(
        descricao='público',
        cor=cor
    )

    cor, created = Cor.objects.get_or_create(
        nome='azul-0',
    )

    leg2, created = Legenda.objects.get_or_create(
        descricao='privado',
        cor=cor
    )

    ld, created = LayerDefinition.objects.get_or_create(
        nome='carater_imovel',
        nome_visualizacao='Caráter do Imóvel',
    )

    ld.legendas.add(leg1, leg2)
    ld.save()

    ###############################################

    cor, created = Cor.objects.get_or_create(
        nome='verde-0',
        cod='#00bd06'
    )

    leg1, created = Legenda.objects.get_or_create(
        descricao='rural',
        cor=cor
    )

    cor, created = Cor.objects.get_or_create(
        nome='cinza-0',
    )

    leg2, created = Legenda.objects.get_or_create(
        descricao='urbana',
        cor=cor
    )

    ld, created = LayerDefinition.objects.get_or_create(
        nome='zona',
        nome_visualizacao='Zona',
    )

    ld.legendas.add(leg1, leg2)
    ld.save()

    ###############################################

    cor, created = Cor.objects.get_or_create(
        nome='vemelho-0',
        cod='#00bd06'
    )

    leg1, created = Legenda.objects.get_or_create(
        descricao='sim',
        cor=cor
    )

    cor, created = Cor.objects.get_or_create(
        nome='branco-0',
        cod='#ffffff'
    )

    leg2, created = Legenda.objects.get_or_create(
        descricao='não',
        cor=cor
    )

    ld, created = LayerDefinition.objects.get_or_create(
        nome='pandemia',
        nome_visualizacao='Pandemia',
    )

    ld.legendas.add(leg1, leg2)
    ld.save()

    ###############################################

