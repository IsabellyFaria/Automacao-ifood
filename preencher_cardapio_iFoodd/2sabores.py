import keyboard
import pyautogui
import pyperclip
import time
pyautogui.PAUSE=0.6
def adiciona_complemento(item, descricao,preco='0'):
    pyautogui.click(1351,464)
    time.sleep(3)
    pyautogui.click(1383,558)
    pyautogui.click(1390,453)
    time.sleep(1)
    pyautogui.click(1384,621)
    pyautogui.moveTo(1309, 598, duration=0.3)  # move lentamente
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
                        
    linha = linha.split('|')
    #preco = linha[1].strip()  
    item  = "1/2 Pizza "+linha[0].strip()
    #descricao = linha[1].strip()
    descricao = linha[1].strip()+" Foto Ilustrativa"
    adiciona_complemento(item, descricao) 

pyautogui.alert("Pronto")

keyboard.wait('q')