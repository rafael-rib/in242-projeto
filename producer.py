import paho.mqtt.client as mqtt
import random
import json
from interruptableLoop import InterruptableLoop
from datetime import datetime

# Configura MQTT broker (Docker)
mqtt_client = mqtt.Client()
# mqtt_client.connect('localhost', 1883) # para teste Local
mqtt_client.connect('18.229.94.95', 1883) # Broker no servidor da AWS

# Prepara e envia mensagem para o MQTT Broker do Docker
def envia_mens(quant):
   now = datetime.now()  # Coleta data e hora atual
   horario = now.strftime("%D - %H:%M:%S")
   mensagem = {
      'cliente': 'Inatel',
      'Porta': 'Porta de entrada',
      'Quantidade': quant,
      'Horario': horario
   }
   mqtt_client.publish('in242_projeto', json.dumps(mensagem))
   print(mensagem,'\nMensagem enviada...')

# Gera trigger a cada x segundos
loop = InterruptableLoop(intervalSecs=10)  # Controla delay do triger e comando de parada

while loop.ShouldContinue():        # Continua repetição enquanto não for interrompida manualmente
    sensor = random.randint(0, 15)  # Simula buffer do sensor de contagem a cada 10 segundos
    envia_mens(sensor) # Chama função para envio da mensagem para o broker
    pass

