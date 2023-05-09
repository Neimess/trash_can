import moviepy.editor
import youtube_downloader
def create_podcast(video_name: str, podcast_name: str):
    video = moviepy.editor.VideoFileClip(video_name)
    audio = video.audio
    audio.write_audiofile(podcast_name)

def main():
    create_podcast()

if __name__ == "__main__":
    main()