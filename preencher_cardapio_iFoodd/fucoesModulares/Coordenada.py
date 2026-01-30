""" Esse arquivo contém
* classe que rege o comportamento das coordenadas
* leitura e escrita de coordenadas pré-existentes
Isabelly Faria 21/01/2026 """
import json
class Coordenada:
    def __init__(self, xNovo,yNovo):
        self.x = xNovo
        self.y = yNovo
    def getXY(self):
        return (self.x,self.y)
    def setXY(self,xNovo,yNovo):
        self.x = xNovo
        self.y = yNovo
def carregarCoordenadas():
    with open("coordenadas.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    coords = {}
    for nome, valor in dados.items():
        coords[nome] = Coordenada(valor["x"], valor["y"])

    return coords
def salvar_coordenadas(coords):
    dados = {}
    for nome, coord in coords.items():
        dados[nome] = {
            "x": coord.x,
            "y": coord.y
        }

    with open("coordenadas.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)