import random
import asyncio
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import Application

# Fonction pour générer un numéro de téléphone fictif
def generate_phone_number():
    return f"+336{random.randint(10000000, 99999999)}"

# Commande /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Bienvenue ! Utilisez la commande /generate <nombre> pour générer des numéros de téléphone fictifs. Exemple : /generate 100"
    )

# Commande /generate <nombre>
async def generate(update: Update, context: CallbackContext):
    try:
        # Vérifier si l'utilisateur a bien passé un nombre
        number_of_numbers = int(context.args[0])
        
        # Générer les numéros de téléphone
        phone_numbers = [generate_phone_number() for _ in range(number_of_numbers)]
        
        # Sauvegarder dans le fichier list.txt
        with open("list.txt", "w") as file:
            file.write("\n".join(phone_numbers))
        
        # Envoi du fichier .txt à l'utilisateur
        with open("list.txt", "rb") as file:
            await update.message.reply_text(f"{number_of_numbers} numéros générés avec succès !")
            await update.message.reply_document(file)

    except (IndexError, ValueError):
        # Gestion des erreurs : message si le nombre est invalide
        await update.message.reply_text("Veuillez entrer un nombre valide après la commande /generate. Exemple : /generate 100")
    except Exception as e:
        # Gestion des erreurs génériques
        await update.message.reply_text(f"Une erreur s'est produite : {e}")

# Fonction principale pour démarrer le bot
def main():
    # Remplacez 'YOUR_TOKEN' par votre token d'API Telegram
    application = Application.builder().token("your_token").build()

    # Ajouter les gestionnaires de commande
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("generate", generate))

    # Démarrer le bot sans utiliser asyncio.run()
    application.run_polling()

if __name__ == '__main__':
    # Lancer le bot de manière asynchrone
    main()
