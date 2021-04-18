import os
import csv
import random
import requests
from random import seed
from random import random

# from despejos.load import despejos
# despejos.run()
def run(path="/home/weiglas/git/monitoramento-remocoes/dados",
        file_name="dados-despejos.csv"):

    minLat = -21
    minLon = -42
    maxLat = -17
    maxLon = -39

    with open(os.path.join(path, file_name), 'r') as file:
        reader = csv.reader(file)

        # lista_despejos = []

        for i, row in enumerate(reader):
            if i == 0:
                continue

            despejo = {}

            seed()
            despejo["latitude"] = minLat + (random() * (maxLat - minLat))
            seed()
            despejo["longitude"] = minLon + (random() * (maxLon - minLon))
            despejo["nome_cidade"] = row[1]
            despejo["nome_ocupacao"] = row[2]
            despejo["num_familias"] = row[3]
            despejo["endereco"] = row[4]
            despejo["situacao"] = row[5]
            despejo["pandemia"] = row[6]
            despejo["descricao"] = row[7]
            despejo["dataexistencia"] = row[10]
            despejo["dataameacadespejo"] = row[11]
            despejo["dataparadespejo"] = row[12]
            despejo["carater_imovel"] = row[13]
            despejo["tipologia"] = row[14]
            despejo["responsavel_despejo"] = row[15]
            despejo["motivo_despejo"] = row[16]
            despejo["cod_acao_justica"] = row[17]
            despejo["link_sobre_despejo"] = row[18]
            despejo["assessoria_juridica"] = row[19]
            despejo["movimento_social"] = row[20]

            response = requests.post("http://127.0.0.1:8000/api/despejo/", data=despejo)
            print(response.content)
            # lista_despejos.append(despejo)
    file.close()

