#Importação de bibliotecas
import dht
from machine import Pin
import time

#Configuração do sensor DHT22
d = dht.DHT22(Pin(14))

#Configuração do relé e do LED.
#O relê representa uma vávula d'água e o LED o fluxo de água
valvula = Pin(12, Pin.OUT)
led = Pin(13, Pin.OUT)

#Define o valor mínimo de umidade antes de ativar a válvula de água
umidade_minima = 30

#Loop principal do programa
while True:
    d.measure() #Lê a umidade do solo
    umidade = d.humidity()

    #Verifica se a umidade está abaixo do valor mínimo
    if umidade < umidade_minima:
        print("Umidade baixa. Ativando a válvula de água...") #Ativa a válvula de água
        valvula.value(1)
        led.value(1) #Liga o LED indicando que a água está sendo irrigada
        time.sleep(5) #Deixa a válvula aberta por 5 segundos
        print("Desativando a válvula de água.")
        valvula.value(0) #Desliga a válvula de água
        led.value(0) #Desliga o LED
    else:
        print("Umidade adequada. A planta não precisa ser irrigada.")
        led.value(0) #Desliga o LED indicando que a planta está com umidade suficiente

    time.sleep(10) #Espera 10 segundos antes de fazer a próxima leitura