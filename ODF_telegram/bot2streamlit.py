import asyncio
from telethon import TelegramClient
import streamlit as st

# Configuration pour le compte utilisateur
API_ID = "25244364"
API_HASH = "23c7042964c6962724f61975f832f055"
SESSION_NAME = "ODF0001"

# Nom d'utilisateur du bot externe
TARGET_BOT_USERNAME = "@DBsearch_UA_Bot"  # Remplacez par le nom du bot souhaité

# Création d'une boucle asyncio dédiée
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Initialiser le client Telegram avec la boucle dédiée
telethon_client = TelegramClient(SESSION_NAME, API_ID, API_HASH, loop=loop)


async def query_bot(query: str) -> str:
    """
    Envoie une requête au bot Telegram et récupère la réponse.
    """
    try:
        # Envoyer un message au bot
        await telethon_client.send_message(TARGET_BOT_USERNAME, query)

        # Attendre une réponse (ajuster le temps si nécessaire)
        await asyncio.sleep(2)

        # Lire la dernière réponse du bot
        async for message in telethon_client.iter_messages(TARGET_BOT_USERNAME, limit=1):
            return message.text

    except Exception as e:
        return f"Erreur lors de la requête : {e}"


def run_query_bot(query: str) -> str:
    """
    Wrapper pour exécuter les fonctions asynchrones dans une boucle d'événements.
    """
    return loop.run_until_complete(query_bot(query))


def main():
    # Titre du tableau de bord
    st.set_page_config(page_title="Bot Telegram Dashboard", layout="wide")
    st.title("Bot Telegram - Tableau de Bord")

    # Section de saisie utilisateur
    st.sidebar.header("Entrez votre requête")
    query = st.sidebar.text_input("Requête pour le bot", placeholder="Tapez votre message ici")

    # Bouton pour envoyer la requête
    if st.sidebar.button("Envoyer"):
        if query.strip():
            with st.spinner("Envoi de votre requête au bot..."):
                # Exécuter la requête au bot
                response = run_query_bot(query)
                st.success("Requête envoyée avec succès !")
                st.subheader("Réponse du bot :")
                st.write(response)
        else:
            st.error("Veuillez entrer une requête valide.")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Développé par votre équipe professionnelle.**")


if __name__ == "__main__":
    # Démarrer la session Telethon
    with telethon_client:
        main()
