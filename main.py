import pywhatkit
import datetime
import time
import keyboard
import config


# Obtenha o horário atual
agora = datetime.datetime.now()
numero = config.numero()

pywhatkit.sendwhatmsg(f'{numero}', 'essa é uma mensagem automatica, que fiz pelo meu bot!!!', agora.hour, agora.minute + 1)

time.sleep(5)

keyboard.press_and_release('enter')