from moviepy.editor import *
import downloader
import generateFrame


def get_image_clip(line):
    try:
        image = downloader.download_image(line['keyword'])
        if image == "":
            image = "bg.jpeg"
    except Exception as e:
        print(e)
        image = "bg.jpeg"
    # image = downloader.download_image(line['keyword'])
    frame = generateFrame.generate_frame(image, line['sentence'])
    duration = len(line['sentence'])/30
    return ((ImageClip(frame)
            .set_duration(duration)
            .set_pos("center")), duration)


def generate_video(lines, title, audio):
    time = 0

    comp_array = []

    print("\n\nDownloading " + str(len(lines)) + " Images ...\n")
    for line in lines:
        image, duration = get_image_clip(line)
        comp_array.append(image.set_start(time).crossfadein(1).crossfadeout(1))
        time += duration-1

    video = CompositeVideoClip(comp_array)
    music = AudioFileClip(audio)
    music = afx.audio_loop(music, duration=video.duration)
    music = afx.audio_fadeout(music, duration=2)
    video = video.set_audio(music)
    video.write_videofile("videos/" + title + ".mp4", threads=4, fps=30)