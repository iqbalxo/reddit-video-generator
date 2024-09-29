import os
from moviepy.editor import VideoFileClip, AudioFileClip

def combine_audio_with_video(audio_file, video_file, output_file):
    try:
        # Load the video and audio files
        video = VideoFileClip(video_file)
        audio = AudioFileClip(audio_file)

        # Trim the video to the length of the audio if audio is shorter
        if video.duration > audio.duration:
            video = video.subclip(0, audio.duration)

        # Set the audio to the video
        final_video = video.set_audio(audio)

        # Write the final video file
        final_video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        print(f"Video saved as: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage (for manual testing)
if __name__ == "__main__":
    os.environ['FFMPEG_BINARY'] = r"C:\Users\Shoaib\ffmpeg-2024-09-19-git-0d5b68c27c-full_build\bin\ffmpeg.exe"
    video_file = r"C:\Users\Shoaib\PycharmProjects\RedditWebsite\gameplays\gp1.mp4"
    audio_file = r"output.mp3"
    output_file = r"final_video.mp4"
    combine_audio_with_video(audio_file, video_file, output_file)
