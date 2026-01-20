#O arquivo contem o conjunto de funções que estrutura a criação de um adicional com a automação, de forma que possa ser utilizado modularmente. Favor, não colocar coordenadas neste arquivo, apenas recebe-las do 'registrarCoordenada.py'
#Isabelly Faria - 19/01/2026
def criarNovoGrupo(nome='Grupo de Adicionais')

def clickarNovoComplemento():
    #clica em novo complemento
    pyautogui.click(1351,464,0.1)
    time.sleep(3)
    #seleciona o tipo 'ingrediente'
    pyautogui.click(1383,558,0.1)
    pyautogui.click(1390,453,0.1)
    time.sleep(1)

def adicionarNome(nome_produto):
    #Clica no campo de nome e realiza movimento
    pyautogui.click(1384,621)
    pyautogui.moveTo(1309, 598, duration=0.3)  # move lentamente
    pyautogui.click()
    #copia o nome
    pyperclip.copy(nome_produto)
    time.sleep(1)
    print(pyperclip.paste())
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")

def adicionarDescricao(descricao_produto):
    #necessário pegar coordenada Correta
    pyautogui.press('tab')
    pyperclip.copy(descricao_produto)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")

def adicionarPreco(preco_produto):
    #preciso pegar coordenada
    pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(preco_produto)
        for i in range(2):
            pyautogui.press('tab')
        pyautogui.press('enter')

def finalizarProduto():
    #preciso pegar coordenada
    for i in range(2):
            pyautogui.press('tab')
        pyautogui.press('enter')