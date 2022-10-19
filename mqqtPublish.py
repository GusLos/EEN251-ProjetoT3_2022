import paho.mqtt.client as mqttClient
import json
from dotenv import dotenv_values
from time import sleep

env = dotenv_values('.env')
# print(env['CHAVE_ACESSO'])

class MqqtPublish ():
    
    def __init__(self) -> None:
        self.env = dotenv_values('.env')
        self.url_to_publish = 'industrial.api.ubidots.com'
        self.device = '/v1.6/devices/raspberrypi3'
        self.access_key = self.env['ACCESS_KEY']
        self.port = 1883
        self.mqtt_client = mqttClient.Client('IApub')
        self.mqtt_client.username_pw_set(self.access_key, password='')
        self.mqtt_client.on_publish = self.on_publish
        self.mqtt_client.connect(self.url_to_publish, port=self.port)
        self.mqtt_client.loop_start()
        pass

    def on_publish(self, client, userdata, result):
        print("[INFO] Published!")

    def publishValue(self, variable: str, value: any) -> None:
        payload = json.dumps({variable: {"value":value}})
        # print({variable: {"value":value}})
        sleep(2)
        self.mqtt_client.publish(self.device, payload)

        pass

    pass


# def on_publish(client, userdata, result):
#     print("[INFO] Published!")

# url_to_publish = 'industrial.api.ubidots.com'
# topico = '/v1.6/devices/raspberrypi3'
# payload = json.dumps({"cozinha": {"value":0}})
# chave_acesso = env['CHAVE_ACESSO']
# porta = 1883

# mqtt_client = mqttClient.Client('IApub')
# mqtt_client.username_pw_set(chave_acesso, password='')
# mqtt_client.on_publish = on_publish
# mqtt_client.connect(url_to_publish, port=porta)
# mqtt_client.loop_start()


# op = int(input('Luz (0 - desliga | 1 - liga)'))

# payload = json.dumps({"cozinha": {"value":op}})
# mqtt_client.publish(topico, payload)


# while True:
#     op = int(input('Luz (0 - desliga | 1 - liga)'))
#     payload = json.dumps({"cozinha": {"value":op}})
#     mqtt_client.publish(topico, payload)
#     pass


if __name__ == '__main__':
    pub = MqqtPublish()
    # while True:
        # op = input('\nLuz (0 - desliga | 1 - liga)\n')
    pub.publishValue('cozinha', 1)
        # pass
    pass