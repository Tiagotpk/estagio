# Estratégia para descobrir qual interruptor controla qual lâmpada
def interruptores_lampadas():
    print("""
    1. Ligue o primeiro interruptor e deixe ligado por alguns minutos.
    2. Desligue o primeiro interruptor e ligue o segundo.
    3. Vá até a sala das lâmpadas:
       - A lâmpada que estiver acesa corresponde ao segundo interruptor.
       - A lâmpada que estiver apagada, mas quente, corresponde ao primeiro interruptor.
       - A lâmpada que estiver apagada e fria corresponde ao terceiro interruptor.
    """)
interruptores_lampadas()
