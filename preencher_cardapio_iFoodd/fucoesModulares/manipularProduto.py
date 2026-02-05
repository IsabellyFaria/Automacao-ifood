"""O arquivo contem o conjunto de funções que estrutura a criação e edição de um produto no iFood com a automação.
* Essa função cria apenas o produto, para que os adicionais sejam criados, usar em colaboração com o arquivo 'criarAdicional.py'.
* Nesse caso, criar um produto colocar nome, descrição e preço.
* Editar um produto, alterar o nome, descrição e preço.
* Favor, não colocar numeros de coordenadas fixas no código, usar o arquivo coordenada.json para tal.
* Dar preferência em usar e criar funções para manter a organização e limpeza do script.
Isabelly Faria - 05/02/2026 """
import atalhosPyautogui
import Coordenada
import time
import pyperclip
coordenadas = Coordenada.carregarCoordenadas()
def esperarCarregamentoPagina(esperar_segundos=5,descricao_esperada="Descrição do produto",repeticao=0, acao=0):
    time.sleep(5)  # Espera 5 segundos para o carregamento da página
    match acao:
        case 0:
            coordenada = 'campo_descricao_criar_produto'
        case 1:
            coordenada = 'campo_descricao_editar_produto_1'
        case 2:
            coordenada = 'campo_descricao_editar_produto_2'
    atalhosPyautogui.copiar(coordenadas[coordenada])
    conteudo = pyperclip.paste()
    if conteudo.strip() == descricao_esperada:
        return True
    else:
        if repeticao >= 5:
            print("Não foi possivel reconhecer a descrição do produto, iremos recalibrar!")
            return False
        esperarCarregamentoPagina(esperar_segundos,descricao_esperada,repeticao + 1, acao)
def criarNomeDecricao(nome_produto,descricao_produto,preco_produto,acao=0):
    match acao:
        case 0:
            coordenada_nome = ['campo_nome_criar_produto','campo_descricao_criar_produto']
        case 1:
            coordenada_nome = ['campo_nome_editar_produto_1','campo_descricao_editar_produto_1']
        case 2:
            coordenada_nome = ['campo_nome_editar_produto_2','campo_descricao_editar_produto_2']
    #adiciona o nome do produto
    pyperclip.copy(nome_produto)
    print(pyperclip.paste())
    time.sleep(0.5)
    atalhosPyautogui.colar(coordenadas['campo_nome_criar_produto'])
    #adiciona a descrição do produto
    pyperclip.copy(descricao_produto)
    time.sleep(0.5)
    atalhosPyautogui.colar(coordenadas['campo_descricao_criar_produto'])
def prosseguirPagina():
    #Clica no botão de prosseguir
    atalhosPyautogui.clickar(coordenadas['btn_prosseguir_produto'])
def adicionarPreco(preco_produto,desconto_produto):
    #Abre a seção de preço
    time.sleep(2)
    atalhosPyautogui.clickar(coordenadas['texto_nome_categoria_criar_produto'])
    #Dá respectivos tabs para chegar no preço
    for _ in range(2):
        pyautogui.press('tab')
    match 
    #Adiciona o preço
    pyperclip.copy(preco_produto)
    time.sleep(0.5)
    atalhosPyautogui.colar(coordenadas['campo_preco_criar_produto'])
    #Adiciona o desconto
    pyperclip.copy(desconto_produto)
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
def conferirPreco(preco_esperado="10,00",coordenada_preco_produto='campo_desconto_criar_produto'):
    atalhosPyautogui.copiar(coordenadas[coordenada_preco_produto])
    conteudo = pyperclip.paste()
    if conteudo.strip() == preco_esperado:
        return True
    else:
        return False
def finalizarProduto():
    #Clica no botão de concluir
    atalhosPyautogui.clickar(coordenadas['btn_concluir_produto'])
def validarAcao(tipo_operacao):
    match tipo_operacao:
        case 0:
            return 0 #criar produto
        case 1:
            atalhoPyautogui.clickar(coordenadas['texto_nome_produto'],qtd=3)
            pyautogui.hotkey('ctrl', 'c')
            texto = pyperclip.paste()
            if texto == "Produto preparado":
                return 1  #editar produto - primeira opção
            else:
                return 2  #editar produto - segunda opção