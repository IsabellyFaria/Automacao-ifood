import keyboard
import pyautogui
import pyperclip
import time
import math
import somErro
pyautogui.PAUSE=0.6
def adiciona_complemento(item, descricao,preco='0'):
    pyautogui.click(1426,495)
    time.sleep(3)
    pyautogui.moveTo(1309,558,duration=0.2)
    pyautogui.click()
    time.sleep(0.4)
    pyautogui.moveTo(1352,460,duration=0.3)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1352, 603, duration=0.4)  # move lentamente
    pyautogui.click()
    pyperclip.copy(item)
    time.sleep(1)
    print(pyperclip.paste())
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('tab')
    pyperclip.copy(descricao)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    if preco == '0':
        for i in range(4):
            pyautogui.press('tab')
        pyautogui.press('enter')
    else:
        print('Ola')           
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(preco)
        for i in range(2):
            pyautogui.press('tab')
        pyautogui.press('enter')


try:
    with open('pizza.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    time.sleep(2)
    for i, linha in enumerate(linhas, start=1):

        linha = linha.split(' | ')
        item = "1/2 Pizza " + linha[0].strip()
        #preco = f"{(float(linha[1].replace(",","."))):.2f}"
        preco = '0'
        descricao = linha[1]+" Foto Ilustrativa."

        adiciona_complemento(item, descricao, preco)

    somErro.som_sucesso()
    pyautogui.alert("✅ Complementos finalizados com sucesso!")

except Exception as e:
    somErro.som_erro()
    pyautogui.alert(f"❌ ERRO:\n{str(e)}")

keyboard.wait('q')
#