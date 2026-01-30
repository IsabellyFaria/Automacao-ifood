import pyautogui
import time
import pyperclip
import keyboard
import math

pyautogui.PAUSE = 0.5

def esperaCarregar():
    pyautogui.moveTo(1537, 559, duration=0.1)
    pyautogui.doubleClick()
    print(pyautogui.position())
    pyautogui.hotkey("ctrl", "c")
    preco = pyperclip.paste()
    if ',' not in preco:
        time.sleep(5)
        esperaCarregar()

def esperaNome():
    pyautogui.moveTo(1031, 663, duration=0.1)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    descricao = pyperclip.paste()
    if len(descricao) > 500:
        time.sleep(5)
        esperaNome()

def adiciona_item(item, descricao, preco, desconto):
    pyautogui.press('home')
    esperaCarregar()

    # Clica em duplicar item
    pyautogui.moveTo(1662, 554, duration=0.1)
    pyautogui.click()
    for i in range(2):
        pyautogui.press('tab')
    pyautogui.press('enter')

    # Confirma duplicação
    pyautogui.moveTo(1138, 674, duration=0.1)
    pyautogui.click()
    time.sleep(7)

    
    esperaNome()
    pyperclip.copy(item)
    # Nome do item
    pyautogui.moveTo(677, 544, duration=0.1)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    # Descrição
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyperclip.copy(descricao)
    pyautogui.hotkey("ctrl", "v")

    # Visível
    pyautogui.moveTo(1840, 986, duration=0.1)
    pyautogui.click()
    pyautogui.click()

    # Abre preço
    time.sleep(2)
    pyautogui.moveTo(1236, 708, duration=0.1)
    pyautogui.click()

    # Coloca preço e desconto
    pyautogui.moveTo(1289, 417, duration=0.1)
    pyautogui.click()
    pyautogui.typewrite(str(preco))
    pyautogui.press('tab')
    pyautogui.typewrite(str(desconto))
    for i in range(2):
        pyautogui.press('tab')
    pyautogui.press('enter')

    # Salvar
    pyautogui.moveTo(1817, 994, duration=0.1)
    pyautogui.click()
    time.sleep(30)

def criaCardapio():
    pyautogui.hotkey("alt","tab")
    with open('pizza.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    print("Iniciando")
    for i, linha in enumerate(linhas, start=1):
        nome, descricao, preco = linha.strip().split('|')
        descricao = descricao.strip() +" Foto Ilustrativa"
        # Corrige valores
        #desconto_valor = float(desconto_txt) / 100      # 6390 → 63.90
        #desconto_valor += 13.00                         # soma R$15,00
        #preco_valor = desconto_valor * 2                # preço é o dobro
        desconto_valor = math.floor((float(preco)*1))+0.9 
        preco_valor = math.floor(desconto_valor/0.5)+0.9
        item = f"{nome.strip()}"

        adiciona_item(
            item,
            descricao.strip(),
            f"{preco_valor:.2f}".replace('.', ','),     # ex: "157,80"
            f"{desconto_valor:.2f}".replace('.', ',')   # ex: "78,90"
        )

    pyautogui.alert("Pronto")

criaCardapio()
