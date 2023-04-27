# Importação de bibliotecas
from machine import Pin
import time

# Definição do pino de LED como saída
led_pin = Pin(5, Pin.OUT)

# Definição do pino do sensor como entrada
pir_pin = Pin(13, Pin.IN)

# Variável para guardar o estado anterior do sensor
estado_anterior = False

# Loop principal do programa
while True:

    # Verifica se o valor do sensor é igual a 1. Caso seja 1, o loop if se inicia
    if pir_pin.value():
        # Verifica se o estado anterior do sensor era igual a 0
        if not estado_anterior:
            print("MOVIMENTO DETECTADO")
            estado_anterior = True
        led_pin.on() # Liga o LED indicativo

    # Irá ocorrer caso o valor do sensor seja igual a 0
    else:
        # Verifica se o estado anterior do sensor era igual a 1
        if estado_anterior:
            print("ÁREA LIMPA")
            estado_anterior = False
        led_pin.off() # LED indicativo desliga

    time.sleep(0.1) # Tempo de descanso antes da próxima reprodução do loop