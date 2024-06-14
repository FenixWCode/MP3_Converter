import os
from moviepy.editor import VideoFileClip
import const

def create_destination_dir():
    mp3_dir = os.path.join(const.CONTAINER_DIRECTORY, "mp3_files")

    os.makedirs(mp3_dir, exist_ok=True)

    print(f"A directory has been created: {mp3_dir}")
    return mp3_dir

def change_extension(filename):
    name, extension = os.path.splitext(filename)

    return f"{name}.mp3"

def convert(filename):
    destination_dir = create_destination_dir()

    video_file_clip = VideoFileClip(filename)

    audio = video_file_clip.audio

    file_basename = os.path.basename(filename)
    destination_full_path =  os.path.join(destination_dir, change_extension(file_basename))

    audio.write_audiofile(destination_full_path, codec="mp3")

    video_file_clip.close()


