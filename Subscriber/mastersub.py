import time
import os
import base64
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connection result code " + str(rc))


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(client, userdata, msg):
    #print(msg.topic)
    coded_string = msg.payload
    decoded = base64.b64decode(coded_string) 
    filename = 'received.zip' 
    with open(filename, 'wb') as f: 
        f.write(decoded)
   #print(msg.topic + " " + str(msg.payload))
    print("Update File received")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1883, 60)
client.loop_start()
client.subscribe("harsha")

client.on_message = on_message
