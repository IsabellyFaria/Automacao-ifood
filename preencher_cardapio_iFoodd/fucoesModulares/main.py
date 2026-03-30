
from Botao import Botao
from Campo import Campo
from Texto import Texto
import json
import Coordenada

componentes = Coordenada.carregarCoordenadas(json.load(open("coordenadas.json", "r", encoding="utf-8")))

