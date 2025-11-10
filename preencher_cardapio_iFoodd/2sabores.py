import keyboard
import pyautogui
import pyperclip
import time
pyautogui.PAUSE=0.6
def adiciona_complemento(item, descricao,preco='0'):
    pyautogui.click(1270,432)
    time.sleep(3)
    pyautogui.click(1391,527)
    pyautogui.click(1284,437)
    time.sleep(1)
    pyautogui.click(1384,621)
    pyautogui.moveTo(1444, 650, duration=0.3)  # move lentamente
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


with open('pizza.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

for i, linha in enumerate(linhas, start=1):
    #item = "Adicional "+linha.strip()
    #preco = '790'                        
    linha = linha.split('|')
    item  = "1/2 Pizza "+linha[0].strip()
    descricao = linha[1].strip()
    adiciona_complemento(item, descricao) 

pyautogui.alert("Pronto")

keyboard.wait('q')