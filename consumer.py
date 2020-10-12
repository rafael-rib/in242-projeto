import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json

# Configura Cliente do MongoDB do Docker
mongo_client = MongoClient('mongo-db', 27017)
mongo_db = mongo_client['in242_projeto']
mongo_collection = mongo_db['controle_acesso']

def msg_recebida(mqtt_client, userdata, msg):
    print('recebendo mensagem...')
    msg_formatada = json.loads(msg.payload)
    mongo_collection.insert_one(msg_formatada)
    print('mensagem inserida...')

# Configura Assinatura do MQTT do Docker

mqtt_client = mqtt.Client()
mqtt_client.connect('mqtt-broker', 1883)
mqtt_client.on_message = msg_recebida
mqtt_client.subscribe('in242_projeto')
mqtt_client.loop_forever()


