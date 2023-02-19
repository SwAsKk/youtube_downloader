from pytube import YouTube
import moviepy.editor 
import os.path

video_link = input("Введите ссылку на видео")
yt = YouTube(video_link)

print(f"Заголовок: {yt.title}")
add_path_video = '.mp4'
add_path_audio = '.mp3'
name = yt.title
path_of_video = name+add_path_video

ys = yt.streams.get_highest_resolution()
ys.download()
print(path_of_video)
if os.path.exists(path_of_video):
    video = moviepy .editor.VideoFileClip(path_of_video)
    audio = video.audio
    audio.write_audiofile(name + add_path_audio)

print("Загрузка видео завершена")
