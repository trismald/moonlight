from telethon import TelegramClient, events
import asyncio
from dotenv import load_dotenv
import os
import re

# Cargar el archivo .env
load_dotenv()

# Acceder a las variables
api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
my_number = os.getenv("celphone")

# Canal personal donde se enviarán los mensajes detectados
CANAL_PERSONAL = '@errorespreciomex'

# Lista de canales a monitorear
canales_a_monitorear = ['@pruebastrisml2']

# Crear cliente
client = TelegramClient('sesion_monitor', api_id, api_hash)

# Monitorear mensajes en múltiples canales
@client.on(events.NewMessage(chats=canales_a_monitorear))
async def handler(event):
    mensaje = event.message.message.lower()

    # Detectar palabras clave con expresiones regulares
    if re.search(r"\berror\b|\berror de precio\b", mensaje):
        canal_origen = event.chat.title if hasattr(event.chat, 'title') else "Canal desconocido"

        # Mensaje que se enviará al canal personal
        mensaje_completo = (
            f"🔎 **Alerta detectada**\n"
            f"📢 **Canal:** {canal_origen}\n\n"
            f"{event.message.message}"
        )

        # Enviar mensaje al canal personal
        await client.send_message(CANAL_PERSONAL, mensaje_completo)

        print(f"✅ Mensaje reenviado a {CANAL_PERSONAL}")

# Iniciar el cliente
async def main():
    try:
        if not client.is_connected():
            await client.start(my_number)
        print("🤖 Monitoreando mensajes en varios canales...")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

# Ejecutar
asyncio.run(main())
