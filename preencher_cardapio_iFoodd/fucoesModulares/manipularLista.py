"""O arquivo contem o conjunto de funções que manipula produtos na tela da lista de produtos do cardápio.
* Essas funções são usadas para esperar o carregamento da página e selecionar produtos para editar ou duplicar.
* Favor, não colocar numeros de coordenadas fixas no código, usar o arquivo coordenada.json para tal.
* Dar preferência em usar e criar funções para manter a organização e limpeza do script.
Isabelly Faria - 30/01/2026 """
import atalhosPyautogui
import Coordenada
import time
import pyperclip
coordenadas = Coordenada.carregarCoordenadas()
def esperarCarregamentoPagina(esperar_segundos=5,coordenada_verificacao='campo_pesquisa_produto',repeticao=0,preco="10,00"):
    if repeticao >= 5:
        print("A página demorou muito para carregar. Verifique sua conexão ou se o site está fora do ar.")
        return
    time.sleep(5)  # Espera 5 segundos para o carregamento da página
    atalhosPyautogui.copiar(coordenada_verificacao)
    conteudo = pyperclip.paste()
    if conteudo.strip() != preco:
        esperarCarregamentoPagina(esperar_segundos,coordenada_verificacao,repeticao + 1,preco)
def selecionarProdutoNaLista(posicao_produto=0):
    