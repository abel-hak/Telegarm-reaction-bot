import tweepy
import time
import os

# Load API credentials from environment variables for better security
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Verify credentials
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication", e)
    exit()

# Function to delete old tweets
def delete_old_tweets():
    tweets = api.user_timeline(count=200, tweet_mode="extended")  # Fetch up to 200 of the most recent tweets
    
    while tweets:
        for tweet in tweets:
            try:
                print(f"Deleting tweet ID {tweet.id}: {tweet.full_text[:50]}...")
                api.destroy_status(tweet.id)
                time.sleep(1)  # To respect Twitter's rate limit
            except tweepy.TweepError as e:
                print(f"Failed to delete tweet ID {tweet.id}: {e}")
                if e.api_code == 88:  # Rate limit exceeded
                    print("Rate limit exceeded. Waiting for 15 minutes...")
                    time.sleep(15 * 60)  # Wait for 15 minutes before retrying
            except Exception as e:
                print(f"An unexpected error occurred with tweet ID {tweet.id}: {e}")
        
        # Fetch the next batch
        tweets = api.user_timeline(count=200, tweet_mode="extended")

if __name__ == "__main__":
    confirmation = input("Are you sure you want to delete your old tweets? Type 'yes' to confirm: ")
    if confirmation.lower() == 'yes':
        delete_old_tweets()
        print("All deletions complete.")
    else:
        print("Operation cancelled.")
