import paho.mqtt.client as mqttClient
from dotenv import dotenv_values

env = dotenv_values('.env')

url_to_publish = 'industrial.api.ubidots.com'
topico = '/v1.6/devices/raspberrypi3/cozinha/lv'
chave_acesso = env['CHAVE_ACESSO']
porta = 1883

def on_message(mqttc, obj, msg):
    print("[INFO] value received: {}".format(float(msg.payload)))


def on_subscriber(mqttc, obj, mid, granted_qos):
    print("[INFO] Subscribed!")

mqtt_client = mqttClient.Client('meuProgSubs')
mqtt_client.username_pw_set(chave_acesso, password='')
mqtt_client.connect(url_to_publish, port=porta)
mqtt_client.on_message = on_message
mqtt_client.on_subscribe = on_subscriber
mqtt_client.subscribe(topico, 0)
mqtt_client.loop_start()

while True:
    mqtt_client.loop()
    op = input('digite algo:\n')
    print(f'Sua op = {op}')
    pass