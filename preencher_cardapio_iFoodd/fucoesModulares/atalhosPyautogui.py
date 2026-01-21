"""O arquivo contém funções de ações repetidas multiplas vezes feitas pelos arquivos. 
* Dar preferência em usar e criar funções para manter a organização e limpeza do script
Isabelly Faria - 20/01/2026"""
import pyautogui

def copiar(coordenada_click):
    clickar(coordenada_click)
    pyautogui.hotKey('ctrl','a')
    pyautogui.hotKey('ctrl','c')
def clickar(coordenada_click,qtd=1, btn='left',duracao = 0.1)
    pyautogui.moveTo(coordenada_click[0], coordenada_click[1], duration = duracao)
    pyautogui.click(clicks = qtd , button = btn)
def colar(coordenada_click):
    clickar(coordenada_click, duracao=0.3)
    pyautogui.hotKey('ctrl','v')
