import os
import random
from instabot import Bot

def post_video_with_random_audio(username, password, video_dir, audio_dir):
    bot = Bot()
    bot.login(username=username, password=password)

    # Get a list of video files in the video directory
    video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]

    if not video_files:
        print("No video files found in the specified directory.")
        return

    # Select a random video file
    random_video_file = random.choice(video_files)
    video_path = os.path.join(video_dir, random_video_file)

    # Get a list of audio files in the audio directory
    audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]

    if not audio_files:
        print("No audio files found in the specified directory.")
        return

    # Select a random audio file
    random_audio_file = random.choice(audio_files)
    audio_path = os.path.join(audio_dir, random_audio_file)

    # Upload video
    media_id = bot.upload_video(video_path)

    # Attach random audio to the video
    bot.edit_media(media_id, new_audio=audio_path)

    # Publish the post
    bot.publish_video(media_id)

    print("Video posted successfully!")

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    video_dir = "video/"  # Modify if your video directory is located elsewhere
    audio_dir = "audio/"  # Modify if your audio directory is located elsewhere

    post_video_with_random_audio(username, password, video_dir, audio_dir)
