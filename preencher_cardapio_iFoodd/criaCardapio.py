import pyautogui
import time
import pyperclip
import keyboard
import math
import somErro
pyautogui.PAUSE = 0.5
def duplicar():
    pyautogui.moveTo(1665, 533, duration=0.3)
    pyautogui.click()
    for i in range(2):
        pyautogui.press('tab')
        time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(4)
    # Confirma duplicação
    pyautogui.moveTo(1146, 643, duration=0.1)
    pyautogui.click()
    time.sleep(7)

def esperaCarregar(sucess=0, tentativas=5):
    pyautogui.press('home')
    pyperclip.copy('')
    pyautogui.moveTo(1518, 528, duration=0.1)
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
    pyautogui.moveTo(652, 664, duration=0.1)
    pyautogui.click()
    
    if tentativa > 3:
        pyautogui.moveTo(515, 222, duration=0.1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(1099, 654, duration=0.1)
        pyautogui.click()
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
    pyautogui.moveTo(603, 544, duration=0.1)
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
    pyautogui.moveTo(1817, 979, duration=0.1)
    pyautogui.click()
    pyautogui.click()

    # Abre preço
    time.sleep(2)
    pyautogui.moveTo(628, 696, duration=0.1)
    pyautogui.click()
    for _ in range(3):
        pyautogui.press('tab')
    pyautogui.press("enter")

    # Coloca preço e desconto
    pyautogui.moveTo(1283, 414, duration=0.1)
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
            descricao = descricao.strip() +" Acompanha Guaraná Antarctica 2l. Foto Ilustrativa"
            #desconto_valor = float(preco)
            #preco.replace(",",".").strip()
            desconto_valor = math.floor((float(69.90)+15))+0.9 
            preco_valor = math.floor(desconto_valor/0.5)+0.9

            item = f"Pizza {nome.strip()} Gigante (8 Pedaços) + Guaraná Antarctica 2l"

            adiciona_item(
                item,
                descricao.strip(),
                f"{preco_valor:.2f}".replace('.', ','),
                f"{desconto_valor:.2f}".replace('.', ',')
            )

        somErro.som_sucesso()
        pyautogui.alert("✅ Cardápio finalizado com sucesso!")

    except Exception as e:
        somErro.som_erro()
        pyautogui.alert(f"❌ ERRO:\n{str(e)}")

criaCardapio()
#