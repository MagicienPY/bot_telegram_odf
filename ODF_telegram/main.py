from telethon import TelegramClient, events
import json

# Vos informations d'identification Telegram
api_id = 25244364  # Remplacez 123456 par votre API ID réel fourni par Telegram
api_hash = '23c7042964c6962724f61975f832f055'  # API Hash fourni par Telegram
bot_username = '@DBsearch_UA_Bot'  # Nom d’utilisateur exact du bot tiers

# Initialiser le client Telegram avec une session unique
client = TelegramClient('ODF-OSINT', api_id, api_hash)

async def main():
    # Envoyer un message initial pour interagir avec le bot
    await client.send_message(bot_username, '/start')

    # Gestionnaire d'événements pour capturer les messages du bot
    @client.on(events.NewMessage(from_users=bot_username))
    async def handler(event):
        # Récupérer le contenu du message
        message = event.message.message
        print("Message reçu du bot:", message)

        # Structurer le message en JSON
        data = {
            'bot_response': message
        }

        # Afficher les données en format JSON dans la console
        print("Données JSON formatées :", json.dumps(data, ensure_ascii=False, indent=4))

# Exécuter le client
with client:
    client.loop.run_until_complete(main())
