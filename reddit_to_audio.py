import praw
import pyttsx3
import os

# Set up Reddit API credentials
reddit = praw.Reddit(
    client_id="dNCeF-cc5B416el0nnBTEw",
    client_secret="mv__XeliuyzHLV8SqYtWP6ITk6XJyg",
    user_agent="iqbalxo"
)

# Fetch Reddit post based on URL
def get_reddit_post(url):
    submission = reddit.submission(url=url)
    return submission.title, submission.selftext

# Convert text to audio using pyttsx3 and save it to an MP3 file
def generate_audio(text, output_file):
    engine = pyttsx3.init()

    if not output_file.endswith(".mp3"):
        output_file += ".mp3"

    try:
        engine.save_to_file(text, output_file)
        engine.runAndWait()
    except Exception as e:
        print(f"Error generating audio: {str(e)}")

# Example usage (for manual testing)
if __name__ == "__main__":
    url = input("Enter the Reddit post URL: ")
    title, body = get_reddit_post(url)
    full_text = f"{title}. {body}"
    generate_audio(full_text, "output.mp3")
