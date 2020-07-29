# telegram-sentiment-bot

Runs a simple telegram bot that uses the [Google Cloud Natural Language API](https://cloud.google.com/natural-language/docs/analyzing-sentiment) to analyze sentiment of messages sent to the bot.

## Setup
1.  Open the Telegram App and start a chat with "BotFather" to create a bot and receive API credentials.
2.  Create a Google Cloud Project via the [Google Cloud Console](console.cloud.google.com) and enable billing.
3.  Install the [Google Cloud SDK](https://cloud.google.com/sdk/install)
4.  Follow the instructions after executing 
    ```
    gcloud init
    ````
    This includes selecting the Cloud Project created in the first step.
5.  Now we can create a service account and store its credentials.
    ```
    export GOOGLE_CLOUD_PROJECT="your-project-id"
    gcloud iam service-accounts create nlp-service
    gcloud iam service-accounts keys create nlp.json --iam-account "nlp-service@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com"
    gcloud services enable language.googleapis.com
    ```
6.  Set the required environment variable for the Credentials to the path where you stored nlp.json.
    ```
    export GOOGLE_APPLICATION_CREDENTIALS = path_to/nlp.json
    ````
7.  To start the bot run:
    ```
    python main.py
    ```
