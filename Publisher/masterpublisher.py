import time
import os
import base64
import paho.mqtt.client as mqtt


client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    print("Connection result code " + str(rc))


#stable connection error handling
try:
    client.on_connect = on_connect
    client.connect("127.0.0.1", 1883, 60)
    client.loop_start()
    #file transfer error handling
    try:
        with open('sendfile.zip','rb') as f:
            bytes=f.read()
            encoded = base64.b64encode(bytes)
            f.close()
        client.publish("harsha", encoded)
        print("Update File successfully sent to remote device")
    except:
        print("Update File failed to send")

except:
    print("Couldn't establish connection")


finally:
    time.sleep(4)
    client.loop_stop()
    client.disconnect()
    
    

