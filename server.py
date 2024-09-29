from flask import Flask, request, jsonify, send_file, render_template
from reddit_to_audio import get_reddit_post, generate_audio
from combine_audio_video import combine_audio_with_video
import os

app = Flask(__name__)

# Home route to render the form for URL input
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the video generation process
@app.route('/generate-video', methods=['POST'])
def generate_video():
    print("POST request received")

    # Get the Reddit URL from the POST request
    reddit_url = request.json.get('reddit_url')
    print(f"Received Reddit URL: {reddit_url}")

    if not reddit_url:
        return jsonify({'error': 'Reddit URL is required'}), 400

    try:
        # Fetch Reddit story
        title, body = get_reddit_post(reddit_url)
        full_text = f"{title}. {body}"

        # Generate the audio file
        audio_file = "output.mp3"
        generate_audio(full_text, audio_file)

        # Combine audio with a gameplay video
        video_file = os.path.join(r"C:\Users\Shoaib\PycharmProjects\RedditWebsite\gameplays", "gp1.mp4")
        final_video = "final_video.mp4"
        combine_audio_with_video(audio_file, video_file, final_video)

        # Send back the download link
        return jsonify({'status': 'success', 'video_file': final_video}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to download the video
@app.route('/download/<filename>')
def download_video(filename):
    try:
        file_path = os.path.join(os.getcwd(), filename)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
