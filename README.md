# Reddit Video Generator

## CREATE VIDEOS FROM REDDIT STORIES 🎥

**GENERATE VIDEOS USING TEXT-TO-SPEECH 🎤, COMBINE WITH GAMEPLAY FOOTAGE 🎮, AND DOWNLOAD THE FINAL VIDEO 🎬**

---

### 🚀 Features

- 📝 **Convert Reddit Posts to Audio**: Use Reddit URLs to convert post text into speech.
- 🎮 **Combine Audio with Gameplay**: Attach the generated audio to gameplay video clips.
- 🖥️ **Flask API for Automation**: Integrate the API into other platforms for video generation.
- 📦 **Download Final Video**: Get the video file directly after generation.

---

### 📦 **Installation**

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-repo/reddit-video-generator.git
cd reddit-video-generator
pip install -r requirements.txt
```
---

### ⚙️ Pre-requisites
Python 3.6+: Ensure you have Python installed. Download Python
FFmpeg: Required for handling audio and video processing. Install FFmpeg.
📝 Quick-Start
1. Run the Flask Server
bash
Copy code
python server.py
2. Open the app in your browser
Visit http://127.0.0.1:5000/ to access the app.
3. Generate a Video
Enter a Reddit post URL (e.g., an "Am I the Asshole" post).
The app will fetch the title and text, convert it to audio, and combine it with a gameplay video.
Download the final video when it's ready!

---

### 🎯 Why Choose Reddit Video Generator?
Automates the video creation process from Reddit posts.
Easy integration with your own video ideas or other media.
Perfect for creating engaging content for platforms like TikTok, YouTube, or Instagram.
Simplifies video editing tasks by merging Reddit content with gameplay clips automatically.

---

### 🛠 Dependencies
This project uses the following dependencies:

praw - Reddit API to fetch posts.
pyttsx3 - Converts Reddit post text to speech.
moviepy - Combines audio and video files.
Flask - Serves the project as a web app.
requests - For handling POST requests in the video generation process.

---

### 👤 Author
Created by Muhammad Iqbal. Reach out at me.iqb4l@gmail.com

---

### 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.



