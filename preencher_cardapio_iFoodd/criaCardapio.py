import pyautogui
import time
import pyperclip
import keyboard
import math
pyautogui.PAUSE = 0.5
def duplicar():
    pyautogui.moveTo(1662, 554, duration=0.1)
    pyautogui.click()
    for i in range(2):
        pyautogui.press('tab')
        time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(1.2)
    # Confirma duplicação
    pyautogui.moveTo(1138, 674, duration=0.1)
    pyautogui.click()
    time.sleep(7)

def esperaCarregar(sucess=0, tentativas=5):
    pyperclip.copy('')
    pyautogui.moveTo(1537, 559, duration=0.1)
    pyautogui.doubleClick()
    print(pyautogui.position())  
    pyautogui.hotkey("ctrl", "c")
    preco = pyperclip.paste()
    if preco != "10,00":
        time.sleep(5)
        esperaCarregar()
    elif sucess < 2:
        sucess += 1
        esperaCarregar(sucess)
def esperaNome(tentativa = 0):
    pyautogui.moveTo(1031, 663, duration=0.1)
    pyautogui.click()
    if tentativa > 3:
        esperaCarregar()
        duplicar()
        esperaNome()
    pyperclip.copy('')
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    descricao = pyperclip.paste()
    if descricao != 'Para criar combo':
        time.sleep(5)
        esperaNome(tentativa+1)
    
def adiciona_item(item, descricao, preco, desconto):
    pyautogui.press('home')
    esperaCarregar()

    # Clica em duplicar item
    duplicar()

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
    pyautogui.moveTo(568, 693, duration=0.1)
    pyautogui.click()
    for _ in range(3):
        pyautogui.press('tab')
    pyautogui.press("enter")

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
    time.sleep(15)

def criaCardapio():
    try:
        pyautogui.hotkey("alt","tab")
        with open('pizza.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        print("Iniciando")

        for i, linha in enumerate(linhas, start=1):
            nome, descricao = linha.strip().split('|')
            descricao = descricao.strip() +" Foto Ilustrativa"

            desconto_valor = math.floor((float(54.90)))+0.9 
            preco_valor = math.floor(desconto_valor/0.5)+0.9

            item = f"Pizza {nome.strip()} - Média (6 Pedaços)"

            adiciona_item(
                item,
                descricao.strip(),
                f"{preco_valor:.2f}".replace('.', ','),
                f"{desconto_valor:.2f}".replace('.', ',')
            )

        som_sucesso()
        pyautogui.alert("✅ Cardápio finalizado com sucesso!")

    except Exception as e:
        som_erro()
        pyautogui.alert(f"❌ ERRO:\n{str(e)}")

criaCardapio()
#