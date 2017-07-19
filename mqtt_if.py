import paho.mqtt.client as mqtt
from gpiozero import LED
from time import sleep
led = LED(17)


def dot():
        led.on()
        sleep(1)
        led.off()
        sleep(1)

def dash():
        led.on()
        sleep(0.4)
        led.off()
        sleep(0.5)



def on_message(client, userdata, message):
        print message.payload
	
	if(message.payload =="gomah" ):
		dot()
		dot()		    



def on_connect(client, userdata, flags, code):
        print "connected:" + str(code)
        client.subscribe("test/all")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("moorhouseassociates.com", 1883, 60)




client.loop_forever()



