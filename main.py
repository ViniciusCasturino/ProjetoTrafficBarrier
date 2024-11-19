
import serial
import time
from twilio.rest import Client


arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)

# Configurações da conta Twilio
account_sid = 'ACb36d23d0c86e23417557b9759b017a51'
auth_token = '95358c16b72cd207b96d4d07221df86c'
client = Client(account_sid, auth_token)

# Função para enviar SMS
def enviar_sms():
    message = client.messages.create(
        body="A barreira está obstruída, vá até o local",
        from_='+17723205071',
        to='+5554991080001'
    )
    print("Mensagem enviada com SID:", message.sid)

print("Monitorando o semáforo:")
try:
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').strip()
            if data == "Barreira Obstruída":
                enviar_sms()  # Envia SMS 
                print("Mensagem enviada..")


except KeyboardInterrupt:
    print("Monitoramento interrompido.")
finally:
    arduino.close()
