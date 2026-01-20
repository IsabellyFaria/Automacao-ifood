"""
Módulo de alertas sonoros para automações
Compatível com:
- PyAutoGUI
- Electron (chamado via child_process)
- Execução como .py ou .exe

Windows only (winsound)
"""

import time

def _beep(freq, dur):
    try:
        import winsound
        winsound.Beep(freq, dur)
    except Exception:
        pass  # nunca interrompe a automação


def sucesso():
    """
    Som curto e agradável indicando sucesso
    """
    _beep(900, 150)
    time.sleep(0.05)
    _beep(1200, 200)


def problema():
    """
    Som mais chamativo indicando erro/problema
    """
    _beep(1400, 250)
    time.sleep(0.1)
    _beep(1000, 250)
    time.sleep(0.1)
    _beep(1400, 250)


def aviso():
    """
    Aviso neutro (atenção)
    """
    _beep(1100, 200)
    time.sleep(0.1)
    _beep(1100, 200)