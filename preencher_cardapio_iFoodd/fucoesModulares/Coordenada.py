""" Esse arquivo contém
* classe que rege o comportamento das coordenadas
* leitura e escrita de coordenadas pré-existentes
Isabelly Faria 21/01/2026 """
import json
from Botao import Botao
from Campo import Campo
from Texto import Texto
class Coordenada:
    def __init__(self, xNovo,yNovo):
        self.x = xNovo
        self.y = yNovo
    def getXY(self):
        return (self.x,self.y)
    def setXY(self,xNovo,yNovo):
        self.x = xNovo
        self.y = yNovo
def carregarCoordenadas(dados):
    """Recebe dados JSON e cria componentes organizados por tipo (botão, campo, texto)."""
    botoes = []
    campos = []
    textos = []

    for nome, valor in dados.items():
        coord_clique = Coordenada(valor["x"], valor["y"])
        if nome.startswith("botao"):
            # Para botões, verifica se há coordenada de validação
            coord_valid = None
            if "x_validacao" in valor and "y_validacao" in valor:
                coord_valid = Coordenada(valor["x_validacao"], valor["y_validacao"])
            botoes.append(Botao(coord_clique, coord_valid))
        elif nome.startswith("campo"):
            campos.append(Campo(coord_clique))
        elif nome.startswith("texto"):
            textos.append(Texto(coord_clique))

    return {"botoes": botoes, "campos": campos, "textos": textos}

def salvar_coordenadas(componentes):
    """Recebe uma lista com [botoes, campos, textos] e salva no JSON."""
    botoes, campos, textos = componentes
    dados = {}

    # Salvar botões
    for i, botao in enumerate(botoes):
        nome = f"botao_{i}"
        dados[nome] = {"x": botao.coordenadaClique.x, "y": botao.coordenadaClique.y}
        if botao.coordenadaValidacao and botao.coordenadaValidacao != botao.coordenadaClique:
            dados[nome]["x_validacao"] = botao.coordenadaValidacao.x
            dados[nome]["y_validacao"] = botao.coordenadaValidacao.y

    # Salvar campos
    for i, campo in enumerate(campos):
        nome = f"campo_{i}"
        dados[nome] = {"x": campo.coordenadaClique.x, "y": campo.coordenadaClique.y}

    # Salvar textos
    for i, texto in enumerate(textos):
        nome = f"texto_{i}"
        dados[nome] = {"x": texto.coordenadaClique.x, "y": texto.coordenadaClique.y}

    with open("coordenadas.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)
