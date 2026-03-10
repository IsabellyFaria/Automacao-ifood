""" Este arquivo tem a função de criar um componente do site com coordenadas e comportamentos pré-definidos, para facilitar a construção do código principal.
* Essa é a classe abstrata, ou seja, não deve ser instanciada, apenas herdada.
* Irá definir que todos componentes, independente de sua função, devem ter uma coordenada de clique e um método de validação.
* Tipos diferentes de componentes podem ser clicados e validados de formas diferentes, mas todos devem ter essas funções.
Isabelly Faria 21/01/2026
"""
class Componente:
    def __init__(self, coordenada):
        self.coordenadaClique = coordenada
        self.coordenadaValidacao = coordenada
    def clicar(self):
        pass
    def validar(self):
        pass