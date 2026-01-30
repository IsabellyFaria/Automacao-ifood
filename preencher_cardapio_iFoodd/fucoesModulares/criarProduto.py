"""O arquivo contem o conjunto de funções que estrutura a criação de um produto no iFood com a automação.
* Essa função cria apenas o produto, para que os adicionais sejam criados, usar em colaboração com o arquivo 'criarAdicional.py'.
* Nesse caso, criar um produto colocar nome, descrição e preço.
* Favor, não colocar numeros de coordenadas fixas no código, usar o arquivo coordenada.json para tal.
* Dar preferência em usar e criar funções para manter a organização e limpeza do script.
Isabelly Faria - 30/01/2026 """
import atalhosPyautogui
import Coordenada
import time
import pyperclip
coordenadas = Coordenada.carregarCoordenadas()
def esperarCarregamentoPagina(esperar_segundos=5,):
    time.sleep(5)  # Espera 5 segundos para o carregamento da página