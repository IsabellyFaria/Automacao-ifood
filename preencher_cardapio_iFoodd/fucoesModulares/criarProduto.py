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
def esperarCarregamentoPagina(esperar_segundos=5,descricao_esperada="Descrição do produto",repeticao=0):
    time.sleep(5)  # Espera 5 segundos para o carregamento da página
    atalhosPyautogui.copiar(coordenadas['campo_descricao_produto'])
    conteudo = pyperclip.paste()
    if conteudo.strip() == descricao_esperada:
        return True
    else:
        if repeticao >= 5:
            print("A página demorou muito para carregar. Verifique sua conexão ou se o site está fora do ar.")
            return False
        esperarCarregamentoPagina(esperar_segundos,descricao_esperada,repeticao + 1)
def criarNomeDecricao(nome_produto,descricao_produto,preco_produto):
    #adiciona o nome do produto
    pyperclip.copy(nome_produto)
    print(pyperclip.paste())
    time.sleep(0.5)
    atalhosPyautogui.colar(coordenadas['campo_nome_produto'])
    #adiciona a descrição do produto
    pyperclip.copy(descricao_produto)
    time.sleep(0.5)
    atalhosPyautogui.colar(coordenadas['campo_descricao_produto'])
def prosseguirPagina():
    #Clica no botão de prosseguir
    atalhosPyautogui.clickar(coordenadas['btn_prosseguir_produto'])
def adicionarPreco(preco_produto,desconto_produto):
    #Abre a seção de preço
    time.sleep(2)
    atalhosPyautogui.clickar(coordenadas['btn_abrir_preco_produto'])
    #Adiciona o preço
    pyperclip.copy(preco_produto)
    time.sleep(0.5)
    atalhosPyautogui.colar(coordenadas['campo_preco_produto'])
    #Adiciona o desconto
    pyperclip.copy(desconto_produto)
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
def conferirPreco(preco_esperado="10,00",coordenada_preco_produto='campo_desconto_produto'):
    atalhosPyautogui.copiar(coordenadas[coordenada_preco_produto])
    conteudo = pyperclip.paste()
    if conteudo.strip() == preco_esperado:
        return True
    else:
        return False