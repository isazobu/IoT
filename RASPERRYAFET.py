# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:53:40 2020

@author: ISA
"""

import RPi.GPIO as GPIO
import time
import telepot		
from pprint import pprint
from twilio.rest import Client
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24


# TELEGRAM

bot = telepot.Bot(<BOT TOKEN>)
bot.getMe()

response = bot.getUpdates()
chat_id = response[0]['message']['chat']['id'] # 123456789

# SMS

account_sid = # YOUR TWILIO ID
auth_token = # YOUR TWILIO TOKEN


client = Client(account_sid, auth_token)

# Static Coordinates
x = 41.025782
y = 28.931487
button_count = 0

try:
   
    start_time = [] #hold the time
   

    while True:
       
       
       
         button_state = GPIO.input(23) 
         if button_state == False: #Pressed ?
            # Count it if it's pressed.
            button_count = button_count+1
            
            start_time.append(time.time()) 
            print(start_time)
            if button_count==3:
               # If pressed 3 times, send messages
               GPIO.output(24, True)
               
               bot.sendLocation(chat_id, x, y)
               bot.sendMessage(chat_id,"I'm need help in the location above, please help!")
               
               
               message = client.messages \
                .create(
                        
                     body=("\nPLEASE HELP ME, MY LOCATİON İS latitude:"+  str(x) +  " longitude:" + str(y)),
                     
                     from_= <TWILIO- TEL> ,
                     to= <YOUR-PHONE>
                     
                 )

               print(message.sid)
                              
               
               button_count=0
               print("WARNING, SENT MESSAGE")
                                 
            
            print('Button clicked..',button_count)
            if(len(start_time) > 2):
               start_time = []
               button_count= 0
         if(len(start_time) > 0):
            if (time.time()- start_time[0])> 10:
               start_time = []
               button_count= 0
               
            time.sleep(0.2)
            
         else:
            GPIO.output(24, False)
except:
    GPIO.cleanup()

