import renderer
import summarizer
import music


def start_work(text, title):
    print("\n\n\nStarting...")
    lines = summarizer.get_summary(text)
    if not len(lines) > 0:
        print("***No valid content found***")
        return

    song = music.get_song(text)
    renderer.generate_video(lines, title, song)
