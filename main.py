import editor
import scraper
import os
import shutil


def recreate_environment():
    dirs = [os.getcwd() + "\\downloads\\", os.getcwd() +
            "\\images\\output\\", os.getcwd() + "\\images\\text\\"]

    for folder in dirs:
        shutil.rmtree(folder)
        os.mkdir(folder)


def take_input():
    y = input("Select input mode:\n1.Raw Text\n2.Article url\n")
    if y.isdigit():
        y = int(y)
        if y == 1:
            title = input("Enter Title\n")
            print("Enter Text (Press Ctrl + D to stop):\n")
            text = ""

            while True:
                try:
                    line = input()
                except EOFError:
                    break
                text += line

            editor.start_work(text, title)
        elif y == 2:
            title = input("Enter Title\n")
            url = input("Input Article url\n")
            text = scraper.get_text_from_url(url)
            print(text)
            editor.start_work(text, title)
    else:
        print("Invalid Input")
        take_input()


recreate_environment()
take_input()
