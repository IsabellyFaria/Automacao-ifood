"""O arquivo contém funções de ações repetidas multiplas vezes feitas pelos arquivos. 
* Dar preferência em usar e criar funções para manter a organização e limpeza do script
Isabelly Faria - 20/01/2026"""
import pyautogui

def copiar(coordenada_click):
    clickar(coordenada_click)
    pyautogui.hotKey('ctrl','a')
def clickar(coordenada_click,qtd, btn='left')
    pyautogui.moveTo(coordenada_click[0],coordenada_click[1],0.1)
    pyautogui.click(clicks = qtd , button = btn)

