"""O arquivo contem o conjunto de funções que estrutura a criação de um adicional com a automação.
* Favor, não colocar coordenadas neste arquivo, apenas recebe-las do 'registrarCoordenada.py' 
Isabelly Faria - 19/01/2026 ´´´"""
import atalhosPyautogui
def criarNovoGrupo(nome='Grupo de Adicionais',min=0,max=1):
    '''
    clickar no botão de novo grupo
    clickar criar grupo
    clickar continuar
    clickar ingredietes
    clickar continuar
    clickar campo nome
    preencher
    escolher quantidade
    clickar continuar
    '''

def finalizarGrupo():
    #clickar no botão de concluir
def clickarNovoComplemento():
    #clicka em novo complemento
    atalhosPyautogui.clickar(1351,464)
    time.sleep(3)
    #seleciona o tipo 'ingrediente'
    atalhosPyautogui.clickar(1383,558)
    atalhosPyautogui.clickar(1390,453)
    time.sleep(1)

def adicionarNome(nome_produto):
    #Clica no campo de nome e realiza movimento
    atalhosPyautogui.clickar(1384,621)
    #copia o nome
    pyperclip.copy(nome_produto)
    time.sleep(1)
    print(pyperclip.paste())
    time.sleep(0.5)
    atalhosPyautogui.colar(1309, 598)

def adicionarDescricao(descricao_produto):
    #necessário pegar coordenada Correta
    pyperclip.copy(descricao_produto)
    time.sleep(0.5)
    atalhosPyautogui.colar(FALTA_X, FALTA_Y)

def adicionarPreco(preco_produto):
    #preciso pegar coordenada
    pyautogui.scroll(-300)
    pyperclip.copy(preco_produto)
    time.sleep(0.5)
    atalhosPyautogui.colar(FALTA_X, FALTA_Y)
def finalizarProduto():
    #preciso pegar coordenada
    