import pyautogui
import keyboard
import time
import pyperclip
import mouse
import math
#Variaveis
x0 = 1661
y0 = 522
x1 = 1671
y1 = 604
x2 = 1662
y2 = 653
x3 = 1661
y3 = 644
xN = 1658
yN = 655

# pausa automática de 0.5s após cada ação do pyautogui
pyautogui.PAUSE = 0.45  
def esperaCarregar(y):
    pyautogui.doubleClick(1543,y)
    pyautogui.hotkey("ctrl", "c")
    preco = pyperclip.paste()
    if len(preco)> 9 or "," not in preco:
        time.sleep(5)
        esperaCarregar(y)
def horario():
    pyautogui.moveTo(713,680,0.1)
    pyautogui.click()
    pyautogui.moveTo(1358,266,0.1)
    pyautogui.click()
    pyautogui.moveTo(1833,970,0.1)
    pyautogui.click()
def esperaNome():
    pyautogui.click(1116,550)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    decricao = pyperclip.paste()
    if len(decricao) > 80:
        time.sleep(5)
        esperaNome()
def executar(categoria,valorAdd):
    time.sleep(4)
    esperaNome()
    print(categoria)
    if categoria != "" and valorAdd == 0:
        pyautogui.click(868,517)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        texto = pyperclip.paste()
        if "-" in texto:
            if  "Coca" not in texto:
                #partes = texto.split("-", 1)
                partes = texto.split("-")
                esquerda = partes[0].strip()
                direita = partes[1].strip()
                #novo_texto = esquerda+" Lanche "+direita+" "+categoria
                # Adiciona uma palavra antes do "-"
                esquerda_modificada = esquerda +' '+ categoria
            
                # Junta de novo
                novo_texto = esquerda_modificada + " - " + direita# Altera nome da categoria do Produto
            else:
                #partes = texto.split("-", 1)
                partes = texto.split("Pizza")
                if len(partes) == 2:
                    esquerda = partes[0].strip()+" "
                    direita = partes[1].strip()
                else:
                    esquerda = ""
                    direita = partes[0].strip()
                # Junta de novo
                novo_texto = esquerda + "Pizza "+categoria+" " + direita# Altera nome da categoria do Produto
        else:
            if "Marmita" in texto:
                print("Marmita")
                partes = texto.split("Marmita")
                print(partes)
                novo_texto = categoria+partes[1]
                print(novo_texto)
            else:
                print("else")
                novo_texto =categoria+" "+texto
        pyperclip.copy(novo_texto)
        pyautogui.hotkey("ctrl", "v")
    if valorAdd != 0 or categoria == "":
        # Abre aba 'Disponivel em'
        pyautogui.click(947,378)
        time.sleep(1)
        #horario()
        #Descobre precos
        pyautogui.click(1080,688)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        precoDesconto = math.floor(float((pyperclip.paste()).replace(',','.'))+valorAdd)+0.9
        precoOriginal = math.floor(precoDesconto/0.5)+0.9
        precoDesconto=str(precoDesconto).replace('.','')+"0"
        precoOriginal = str(precoOriginal).replace('.','')+"0"
        # Abre aba para trocar preço e desconto
        pyautogui.moveTo(1130,689,0.1)
        pyautogui.doubleClick()
        
        # Clica 2 vezes no preço
        pyautogui.moveTo(1269,425,1.4)
        pyautogui.doubleClick()
        pyautogui.typewrite(precoOriginal)
        
        pyautogui.press('tab')
        pyautogui.typewrite(precoDesconto)
        
        # Clica no botão de salvar
        pyautogui.click(1810,985)
    pyautogui.click(1803,985)
    time.sleep(11)
def defineCoordenadaAlmodega(i):
    #Coordenadas para clicar no botão
    x=xN
    y=yN
    if i  == 0:
        x=x0
        y=y0
    elif i == 1:
        x=x1
        y=y1
    elif i == 2:
        x=x2
        y=y2
    elif i == 3:
        x=x3
        y=y3
    else:
        x=xN
        y=yN
    coordenada = [x,y]
    return coordenada
    
def executaVarias(qtd,i,categoria,valorAdd):
    for j in range(i,qtd):
        if j > 22:
            time.sleep(5)
        coordenada = defineCoordenadaAlmodega(j)
        esperaCarregar(coordenada[1])
        pyautogui.click(coordenada[0],coordenada[1])
        pyautogui.press('tab')
        pyautogui.press('enter')
        executar(categoria,valorAdd)
    pyautogui.alert("Pronto")