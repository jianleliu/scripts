from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import AudioFileClip
import os
import env


def download_youtube_audio(url, start_time, end_time, output_file):
    try:
        output_file = output_file

        # Download YouTube video.
        print("Downloading YouTube video...")
        yt = YouTube(url)
        video_stream = yt.streams.filter(file_extension="mp4").first()
        video_stream.download()
        if not output_file:
            output_file = yt.title

        # Trim video to the specified time range.
        print("Trimming video to specified time range...")
        clip = VideoFileClip(f"./{yt.title}.mp4")
        trimmed_clip = clip.subclip(start_time, end_time)
        trimmed_clip.write_videofile("trimmed_video.mp4", codec="libx264")

        # Extract audio from trimmed video.
        print("Extracting audio from trimmed video...")
        audio_clip = AudioFileClip("trimmed_video.mp4")
        audio_clip.write_audiofile(f"./output/{output_file}.mp3")

        # Clean up temporary files.
        os.remove(f"{yt.title}.mp4")
        os.remove("trimmed_video.mp4")

        print("Audio extraction complete. Output saved to", output_file)

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    url = env.url
    start_time = env.start_time
    end_time = env.end_time
    output_file = env.output_file

    download_youtube_audio(url, start_time, end_time, output_file)
