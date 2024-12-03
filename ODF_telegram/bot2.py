import asyncio
from telethon import TelegramClient

# Configuration pour le compte utilisateur
API_ID = "25244364"
API_HASH = "23c7042964c6962724f61975f832f055"
SESSION_NAME = "ODF0001"

# Nom d'utilisateur du bot externe que vous voulez interroger
TARGET_BOT_USERNAME = "@DBsearch_UA_Bot"  # Remplacez par le nom du bot souhaité

# Initialiser Telethon avec un compte utilisateur
telethon_client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def query_bot(query: str) -> str:
    """
    Envoie une requête au bot et récupère la réponse.
    """
    try:
        # Envoyer un message au bot
        await telethon_client.send_message(TARGET_BOT_USERNAME, query)
        print("Message envoyé au bot.")

        # Attendre la réponse du bot
        await asyncio.sleep(2)

        # Lire la dernière réponse du bot
        async for message in telethon_client.iter_messages(TARGET_BOT_USERNAME, limit=1):
            return message.text

    except Exception as e:
        return f"Erreur lors de la requête : {e}"


async def main():
    # Démarrer la session Telethon
    async with telethon_client:
        # Demande à l'utilisateur de saisir la requête pour le bot
        user_query = input("Entrez votre requête pour le bot : ")

        # Envoyer la requête au bot et récupérer la réponse
        response = await query_bot(user_query)
        
        # Afficher la réponse du bot
        print(f"Réponse du bot : {response}")


# Exécuter la boucle principale
if __name__ == "__main__":
    asyncio.run(main())
