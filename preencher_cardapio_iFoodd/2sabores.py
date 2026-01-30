import keyboard
import pyautogui
import pyperclip
import time
import math
pyautogui.PAUSE=0.6
def adiciona_complemento(item, descricao,preco='0'):
    pyautogui.click(1426,495)
    time.sleep(3)
    pyautogui.click(1423,557)
    pyautogui.click(1426,465)
    time.sleep(1)
    pyautogui.moveTo(1508, 654, duration=0.3)  # move lentamente
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


with open('complemento.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

for i, linha in enumerate(linhas, start=1):
    
                        
    linha = linha.split('|')
    item = "Acompanhamento "+linha[0].strip()
    preco = "0"
    #preco = f"{(math.floor((float(linha[2].strip())*1))+0.9):.2f}"
    #item  = "1/2 Pizza "+linha[0].strip()
    #descricao = linha[1].strip()
    descricao = linha[1].strip()+" Foto Ilustrativa."
    adiciona_complemento(item, descricao, preco) 

pyautogui.alert("Pronto")

keyboard.wait('q')