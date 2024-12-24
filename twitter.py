def get_latest_tweet(username):
    """Fetches the latest tweet from a Twitter/X account."""
    url = f"https://api.twitter.com/2/tweets?username={username}"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN_HERE"  # Replace with a valid Twitter API Bearer Token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tweets = response.json()
        latest_tweet = tweets['data'][0]['text'] if 'data' in tweets else "No tweets available."
        return latest_tweet
    else:
        return f"Failed to fetch tweets. Status code: {response.status_code}"
