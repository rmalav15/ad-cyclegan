import os

import textwrap
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

FONT_DIR = "/mnt/069A453E9A452B8D/Ram/adGeneration/fonts"
HEAD_DIR = "/mnt/069A453E9A452B8D/Ram/adGeneration/trainHead"
DESC_DIR = "/mnt/069A453E9A452B8D/Ram/adGeneration/trainDisc"

IMAGE_STARTING_INDEX = 1000000
IM_SIZE = 256
HEADLINE_FONT_SIZE = 40
DESCRIPTION_FONT_SIZE = 15
HEAD_LINE_WIDTH = 15
DESC_LINE_WIDTH = 40

BACKGROUND_COLOR = (0, 255, 170)
HEADLINE_COLORS = [(0, 153, 51), (0, 0, 0), (255, 153, 51), (255, 255, 255), (204, 51, 255), (0, 153, 255),
                   (153, 51, 51)]
DESC_COLORS = [(0, 0, 0), (255, 77, 77), (255, 255, 255)]

HEADLINES = [
    "Thick atmosphere",
    "The temperature of the land remains fairly constant.",
    "the Mississippi River",
    "oxygen and minerals",
    "Which are produced during photosynthesis?",
    "Cotton",
    "independent variable",
    "The work of scientist",
    "blood circulation",
    "temperature",
]

DESCRIPTION = [
    "The molecules spread apart and move more slowly.,The molecules spread apart and move more quickly.,",

    "The molecules come together and move more slowly.,The molecules come together and move more quickly.",

    "1708,the nervous system and the digestive system,the digestive system and the circulatory system,the respiratory "
    "system and the nervous system,the muscular system and the nervous system,D,Which two systems of the body are "
    "interacting when a runner sprains his ankle?",

    "the soil the deer the trees the fungi",

    "Hibernation helps an animal avoid being attacked by predators",

    "Iceland overlies a boundary between two tectonic plates that are colliding.,Iceland overlies a "
    "boundary between two tectonic plates that are moving apart.,Iceland is on a single tectonic plate and "
    "is far from any plate boundaries.,Iceland is on a single"
    " tectonic plate that is moving under another plate.,B,Which statement best explains why Iceland has so "
    "many active volcanoes?",

    "rises to a higher temperature,remains at the lower temperature,returns to the initial or room "
    "temperature,alternates between high and low temperature",

    "221,kinetic energy,nuclear energy,chemical energy,mechanical energy,C,Waste Not: Energy "
    "from Garbage and Sewage A hundred years ago, gas was collected from rotting sewage and "
    "used to light street lamps. New technologies hope to update this concept-tapping garbage "
    "as well as human waste-for an energy-hungry world. One promising device is called a microbial "
    "fuel cell. It makes electricity much like a hydrogen fuel cell, but it runs off wastewater. "
    "Sewage-eating bacteria drive a chemical process that generates current and, as a bonus, "
    "helps purify the water. Bruce Logan of Pennsylvania State University and his colleagues have "
    "constructed small microbial fuel cells, no bigger than a can that can power various devices, "
    "including a small fan. ""If you had 100,000 people and you treat their sewage, you could get up "
    "to 2.3 megawatts of continuous power, which is enough to supply electricity for 1,500 homes, Logan said. "
    "A megawatt is one million watts. A self-sufficient water-treatment device is also something that NASA is "
    "interested in. Bruce Rittman of Northwestern University is currently devising a microbial fuel cell "
    "that could be used on manned space missions. ""You have to recycle everything up in space, Rittman said. "
    "You want to capture food waste and human waste, as well as recycle water. A microbial fuel cell"
    " has some advantages over the more traditional method, called an anaerobic digester, which collects "
    "the methane, or biogas, that bacteria belch out when they consume organic material in the absence of "
    "oxygen. The methane is later burned to turn a turbine generator. Instead of "

]


def draw_single(text, font, color, line_width, canvas_size=256, x_offset=10, y_offset=20):
    img = Image.new("RGB", (canvas_size, canvas_size), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    lines = textwrap.wrap(text, width=line_width)
    y_text = y_offset

    for line in lines:
        width, height = font.getsize(line)
        draw.text((x_offset, y_text), line, font=font, fill=color)
        y_text += height

    return img


def draw_multiple(text_list, im_size, fonts_list, font_size, colors, save_path, line_width):
    image_count = 0
    for font_ttf in fonts_list:
        font = ImageFont.truetype(font_ttf, size=font_size)
        for text in text_list:
            for color in colors:
                img = draw_single(text, font, color, line_width, canvas_size=im_size)
                img.save(os.path.join(save_path, str(IMAGE_STARTING_INDEX + image_count) + ".jpg"))
                image_count += 1


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == "__main__":
    _fonts_list = [os.path.join(FONT_DIR, file) for file in os.listdir(FONT_DIR) if file.endswith(".ttf")]

    make_dir(DESC_DIR)
    draw_multiple(DESCRIPTION, IM_SIZE, _fonts_list, DESCRIPTION_FONT_SIZE, DESC_COLORS, DESC_DIR, DESC_LINE_WIDTH)

    make_dir(HEAD_DIR)
    draw_multiple(HEADLINES, IM_SIZE, _fonts_list, HEADLINE_FONT_SIZE, HEADLINE_COLORS, HEAD_DIR, HEAD_LINE_WIDTH)