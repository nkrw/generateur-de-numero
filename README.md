# 🎲 Générateur de Numéros

Bienvenue dans le **Générateur de Numéros**, un projet conçu pour générer des numéros de téléphone fictifs de manière efficace et automatisée via un bot Telegram.

## 🚀 Fonctionnalités
- Génération de numéros de téléphone fictifs français
- Prise en charge des commandes Telegram pour interagir avec le bot
- Génération de plusieurs numéros en une seule commande
- Sauvegarde des numéros générés dans un fichier texte
- Envoi automatique du fichier contenant les numéros générés

## 🛠️ Installation

### Prérequis
- [Python 3.x](https://www.python.org/downloads/) installé sur votre machine
- Un bot Telegram avec un token API valide
- Les bibliothèques Python requises : `python-telegram-bot`, `asyncio`

### Étapes d’installation
1. Clonez ce dépôt GitHub :
   ```sh
   git clone https://github.com/votre-utilisateur/generateur-numero.git
   ```
2. Accédez au dossier du projet :
   ```sh
   cd generateur-numero
   ```
3. Installez les dépendances :
   ```sh
   pip install -r requirements.txt
   ```

## 🎯 Utilisation

### Lancement du bot
Exécutez le script avec la commande suivante :
```sh
python nums.py
```

### Commandes disponibles
| Commande            | Description |
|--------------------|-------------|
| `/start`          | Démarre le bot et affiche un message de bienvenue |
| `/generate <n>`   | Génère `n` numéros de téléphone fictifs et les enregistre dans un fichier |

### Exemple d’utilisation
Envoyez la commande suivante à votre bot Telegram :
```sh
/generate 1000
```
Le bot générera alors 1000 numéros et enverra un fichier `list.txt` contenant ces numéros.

## 📜 Licence
Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Contributeurs
- **[NKR_W]([https://github.com/votre-utilisateur](https://t.me/NKR_W))** - Créateur et développeur principal

Les contributions sont les bienvenues ! N’hésitez pas à soumettre une **Pull Request** ou à signaler un problème dans l’onglet **Issues**.

## 📬 Contact
Pour toute question, contactez-moi via **[@NKR_W]([mailto:email@example.com](https://t.me/NKR_W))** ou ouvrez une issue sur GitHub.

---
✨ *Merci d'utiliser le Générateur de Numéros !*
