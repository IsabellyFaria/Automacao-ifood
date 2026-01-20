'''Nesse arquivo, será lido as coordenadas e também alteradas. 
* Apenas definir coordenadas usando as funções abaixo.
Isabelly Faria - 20/01/2026'''
import alertas
import pyautogui
import pyperclip
import atalhosPyautogui
import keyboard
import conexao
coordenadasCriarAdicional= []
#Função para validar se a execução está sendo feita de forma correta
def validarExecucao(gabarito,campo, coordenadas_click){
    #Aqui irá clicar no campo recém preenchido e se estiver diferente, irá emitir um ruido sonoro.
    coordenada_campo = campo.getXY()
    atalhosPyautogui.copiar(coordenada_campo)
    campo_preenchido = pyperclip.paste()
    if gabarito.strip() != campo_preenchido.strip():
        alertas.problema()
        #AVISA O FRONT
          # avisa o Electron
        conexao.setInformacao(mensagem = "ERRO_VALIDACAO_CAMPO")
        # aguarda liberação do JS
        aguardarConfirmacaoJS()

        salvarCoordenada(coordenada_campo, resposta)
        return False
    return True
}
#
def aguardarConfirmacaoJS():
    conexao.getInformacao(mensagem = "AGUARDANDO_CONFIRMACAO")
    conexao.getInformacao(mensagem = "OK_VISUAL")
#Função para buscar a coordenada correta após não validação
def buscarCoordenada():
    print("AGUARDANDO_CLIQUE_DIREITO", flush=True)

    keyboard.wait("right mouse")
    x, y = pyautogui.position()

    print(f"COORDENADA_CAPTURADA:{x},{y}", flush=True)
    return (x, y)
#Função para salvar a coordenada correta após busca
def salvarCoordenada(coordenada_campo,resposta):
    campo.setXY(resposta[0], resposta[1])



