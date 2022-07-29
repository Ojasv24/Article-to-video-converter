from PIL import Image, ImageDraw, ImageFont
import textwrap, random


def generate_text(text, save):
    lines = textwrap.wrap(text, width=70)
    font = ImageFont.truetype('comicbd.ttf', 30)

    m_height = 0
    m_width = 0

    for line in lines:
        width, height = font.getsize(line)

        if width > m_width:
            m_width = width

        m_height += height

    img = Image.new('RGBA', (m_width + 16, m_height + 16), (255, 255, 255, 128))
    draw = ImageDraw.Draw(img)

    y_text = 0

    for line in lines:
        width, height = font.getsize(line)
        draw.text(((m_width - width) / 2, y_text), line, font=font, fill=(0, 0, 0))
        y_text += height

    img.save('images/text/' + save)

    return 'images/text/' + save


def generate_frame(image, sentence):
    save_path = str(random.randint(0, 1000000000000)) + ".png"
    text_img = generate_text(sentence, save_path)

    black_bg = Image.new('RGB', (1200, 600), (0,0,0))
    background = Image.open(image)
    foreground = Image.open(text_img)

    hpercent = (700 / float(background.size[1]))
    wsize = int((float(background.size[0]) * float(hpercent)))

    background = background.resize((wsize, 700))

    b_width, b_height = background.size
    f_width, f_height = foreground.size

    offset = ((1200 - f_width) // 2, (600 - f_height) // 2)
    offset_bg = ((1200 - b_width) // 2, (600 - b_height) // 2)

    black_bg.paste(background, offset_bg)
    black_bg.paste(foreground, offset, foreground)

    black_bg.save("images/output/"+save_path)
    return "images/output/"+save_path
