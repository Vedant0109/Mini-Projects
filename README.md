This are some Projects of mine which are not too big to have their own repo 

WhatsApp Message Sender AKA WhatsApp.py
-

This is designed for sending Message to your WhatsApp account from Code IDE
Dependecies->
- Installing pywhatkit module [ pip install pywhatkit]
- Login to your WhatsApp account on your default browser


Parameters-->
- In pywhatkit.sendwhatmsg( 1st parameter, 2nd parameter, 3rd parameter, 4th parameter)
- 1st - Your phone number Ex) "+911234567890" [ for India] It should be a string so using "" are must
- 2nd - Your Message Ex) "Hello" It also should be a string
- 3rd - Your Time in hours in 24 hour format Ex) 19 as integer so no need to use ""
- 4th - Minute Ex) 3 as integer [ Note - 3 minutes more than the actual time for convinience]

so example usage:
- pywhatkit.sendwhatmsg("+911234567890" , "Hello", 19 , 3)


   
