import paho.mqtt.client as mqttClient
import json
# from time import sleep
# from dotenv import load_dotenv
from dotenv import dotenv_values

# load_dotenv()
env = dotenv_values('.env')
# print(env['CHAVE_ACESSO'])

def on_publish(client, userdata, result):
    print("[INFO] Published!")

url_to_publish = 'industrial.api.ubidots.com'
topico = '/v1.6/devices/raspberrypi3'
# payload = json.dumps({"cozinha": {"value":0}})
chave_acesso = env['CHAVE_ACESSO']
porta = 1883

mqtt_client = mqttClient.Client('meuProg')
mqtt_client.username_pw_set(chave_acesso, password='')
mqtt_client.on_publish = on_publish
mqtt_client.connect(url_to_publish, port=porta)
mqtt_client.loop_start()


# op = int(input('Luz (0 - desliga | 1 - liga)'))

# payload = json.dumps({"cozinha": {"value":op}})
# mqtt_client.publish(topico, payload)


while True:
    op = int(input('Luz (0 - desliga | 1 - liga)'))
    payload = json.dumps({"cozinha": {"value":op}})
    mqtt_client.publish(topico, payload)
    pass
