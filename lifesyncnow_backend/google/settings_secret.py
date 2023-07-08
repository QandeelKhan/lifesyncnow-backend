from dotenv import load_dotenv
load_dotenv()

# Add the Google API key
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP_ID': 'your-google-api-key',
        'APP_SECRET': 'your-google-client-secret',
    }

}

TWITTER_CONSUMER_KEY = "your_consumer_key"
TWITTER_CONSUMER_SECRET = "your_consumer_secret"
