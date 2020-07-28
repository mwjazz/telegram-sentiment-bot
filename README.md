# telegram-sentiment-bot

Runs a simple telegram bot that uses the [Google Cloud Natural Language API](https://cloud.google.com/natural-language/docs/analyzing-sentiment) to analyze sentiment of messages sent to the bot.

## Setup
1.  Create a Google Cloud Project via the [Google Cloud Console](console.cloud.google.com) and enable billing.
2.  Install the [Google Cloud SDK](https://cloud.google.com/sdk/install)
3.  Follow the instructions after executing 
    ```
    gcloud init
    ````
    This includes selecting the Cloud Project created in the first step.
4.  Now we can create a service account and store its credentials.
    ```
    export GOOGLE_CLOUD_PROJECT="your-project-id"
    gcloud iam service-accounts create nlp-service
    gcloud iam service-accounts keys create nlp.json --iam-account "nlp-service@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com"
    gcloud services enable language.googleapis.com
    ```
5.  Set the required environment variable for the Credentials to the path where you stored nlp.json.
    ```
    export GOOGLE_APPLICATION_CREDENTIALS = path_to/nlp.json
    ```
    
To start the bot run:
```
python run.py
```
