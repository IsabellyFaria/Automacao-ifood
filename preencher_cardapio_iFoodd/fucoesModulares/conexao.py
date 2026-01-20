'''O arquivo será o responsavél por reunir todas ações do python que entram em contato com o frontend
Isabelly Faria - 20/01/2026'''
def setInformacao(mensagem, flushCampo = True):
    print(mensagem, flush=flushCampo)
def getInformacao(mensagem):
    for linha in sys.stdin:
        if linha.strip() == mensagem:
            break
    
    

    