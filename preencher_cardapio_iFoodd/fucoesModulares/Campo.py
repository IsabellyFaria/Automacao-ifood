""" Classe herdeira de componente, tem propósito de reger o comportamento dos campos de texto, afim de padronizar e facilitar a construção do código principal.
* Tem a função de clicar e validar um campo de texto, ou seja, clicar na coordenada pré-definida e validar se o clique foi bem sucedido, copiando alguma informação e verificando se a informação copiada é a esperada.
Isabelly Faria 21/01/2026
"""
import atalhosPyautogui
import pyperclip
from Componente import Componente

class Campo(Componente):
    def __init__(self, coordenadaClique, coordenadaValidacao=None, textoValidacao=None, textoInserido=None):
        """Campo usa coordenada de clique e (opcional) coordenada de validação."""
        super().__init__(coordenadaClique, coordenadaValidacao)
        self.textoValidacao = textoValidacao
        self.textoInserido = textoInserido

    def clicar(self):
        atalhosPyautogui.clickar(self.coordenadaClique, texto=self.textoInserido)
        pass

    def validar(self):
        atalhosPyautogui.colar(self.coordenadaValidacao)
        texto_copiado = pyperclip.paste()
        return texto_copiado == self.textoValidacao
