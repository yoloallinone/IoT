import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

def on(pin):
    GPIO.output(pin,GPIO.HIGH)
    return

def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def handle(msg):
    chat_id=msg['chat']['id']
    command=msg['text']

    print('Got Command: %s'%command)

    if command =='on':
        bot.sendmessage(chat_id,on(11))
    elif command == 'off':
        bot.sendmessage(chat_id,off(11))

bot=telepot.Bot('Bot Token')
bot.message_loop(handle)
print('I am listing')

while True:
    try:
        time.sleep(10)
        
    except KeyboardInterrupt:
        print("\n Program Interrupt")
        GPIO.cleanup()
        exit()

    except:
        print("other error or exception occured")
        GPIO.cleanup()
        
