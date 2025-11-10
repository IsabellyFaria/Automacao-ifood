import pyautogui
import time
import pyperclip
import keyboard

pyautogui.PAUSE = 0.5

def esperaCarregar():
    pyautogui.moveTo(1542, 525, duration=0.5)
    pyautogui.doubleClick()
    print(pyautogui.position())
    pyautogui.hotkey("ctrl", "c")
    preco = pyperclip.paste()
    if ',' not in preco:
        time.sleep(5)
        esperaCarregar()

def esperaNome():
    pyautogui.moveTo(1031, 663, duration=0.5)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    descricao = pyperclip.paste()
    if len(descricao) > 80:
        time.sleep(5)
        esperaNome()

def adiciona_item(item, descricao, preco, desconto):
    pyautogui.press('home')
    esperaCarregar()

    # Clica em duplicar item
    pyautogui.moveTo(1668, 525, duration=0.5)
    pyautogui.click()
    for i in range(2):
        pyautogui.press('tab')
    pyautogui.press('enter')

    # Confirma duplicação
    pyautogui.moveTo(1146, 665, duration=0.5)
    pyautogui.click()
    time.sleep(7)

    pyperclip.copy(item)
    esperaNome()

    # Nome do item
    pyautogui.moveTo(1067, 552, duration=0.5)
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
    pyautogui.moveTo(1840, 986, duration=0.5)
    pyautogui.click()
    pyautogui.click()

    # Abre preço
    time.sleep(2)
    pyautogui.moveTo(1337, 707, duration=0.5)
    pyautogui.click()

    # Coloca preço e desconto
    pyautogui.moveTo(1277, 421, duration=0.5)
    pyautogui.click()
    pyautogui.typewrite(str(preco))
    pyautogui.press('tab')
    pyautogui.typewrite(str(desconto))
    for i in range(2):
        pyautogui.press('tab')
    pyautogui.press('enter')

    # Salvar
    pyautogui.moveTo(1817, 994, duration=0.5)
    pyautogui.click()
    time.sleep(18)

def criaCardapio():
    with open('pizza.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    print("Iniciando")
    for i, linha in enumerate(linhas, start=1):
        nome, descricao, desconto_txt = linha.strip().split('|')

        # Corrige valores
        desconto_valor = float(desconto_txt) / 100      # 6390 → 63.90
        desconto_valor += 13.00                         # soma R$15,00
        preco_valor = desconto_valor * 2                # preço é o dobro

        item = f"Combo Pizza {nome.strip()} + Guaraná 1,5l"

        adiciona_item(
            item,
            descricao.strip(),
            f"{preco_valor:.2f}".replace('.', ','),     # ex: "157,80"
            f"{desconto_valor:.2f}".replace('.', ',')   # ex: "78,90"
        )

    pyautogui.alert("Pronto")

criaCardapio()
