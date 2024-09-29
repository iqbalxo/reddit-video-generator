import requests

url = "http://127.0.0.1:5000/generate-video"
new_reddit_url = "https://www.reddit.com/r/AmItheAsshole/comments/1fot3gk/aita_for_dropping_off_my_friends_dog_at_a_doggy/"

payload = {
    "reddit_url": new_reddit_url  # Ensure this is the correct URL
}

response = requests.post(url, json=payload)

# Print the server's response to confirm success
print(f"Server response: {response.json()}")
