""" Classe que será base de todos tipos de grupo de ação do ifood 
*  Determina ações básicas, como unir o click com  a validação, para facilitar a construção do código principal.
*  A classe é genérica, ou seja, pode ser usada para qualquer tipo de grupo
Isabelly Faria 21/01/2026"""

class Grupo():
    def __init__(self, componentes):
        self.componentes = componentes
        
    def executarComponente(self, componente):  
        componente.clicar()
        if not componente.validar():
            print(f"Validação falhou para {componente}")
            return False
        return True