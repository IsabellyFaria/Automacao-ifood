""" Classe herdeira de componente, tem propósito de reger o comportamento dos blocos de texto, afim de padronizar e facilitar a construção do código principal.
* Tem a função de clicar e validar um blocos de texto, ou seja, clicar na coordenada pré-definida e validar se o clique foi bem sucedido, copiando alguma informação e verificando se a informação copiada é a esperada.
Isabelly Faria 21/01/2026
"""
import atalhosPyautogui
import pyperclip
from Componente import Componente

class Texto(Componente):
    def __init__(self, coordenadaClique, coordenadaValidacao=None, textoValidacao=None):
        """Texto usa coordenada de clique e (opcional) coordenada de validação."""
        super().__init__(coordenadaClique, coordenadaValidacao)
        self.textoValidacao = textoValidacao

    def clicar(self):
        atalhosPyautogui.copiar(self.coordenadaClique,qtd=3)

    def validar(self):
        texto_copiado =self.clicar()
        return texto_copiado == self.textoValidacao
