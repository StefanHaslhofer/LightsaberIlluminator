from time import sleep

from PIL import ImageGrab
from screeninfo import get_monitors

# snapshot a certain area of the screen and interpret pixel colors
from send_serial import write_to_serial


def read_screen_color():
    screen = get_monitors()[1]
    pixel_hex_values = []

    # do not observe left/right fifth and top/bottom sixth of screen
    padding_w = round(screen.width / 4)
    padding_h = round(screen.height / 6)
    px = ImageGrab.grab(bbox=(
        padding_w, padding_h, screen.width - padding_w, screen.height - padding_h)).load()
    for x in range(0, screen.width - 2 * padding_w, 5):
        for y in range(0, screen.height - 2 * padding_h, 5):
            color = px[x, y]
            pixel_hex_values.append('%02x%02x%02x' % color)

    return pixel_hex_values


# searches for bright or unusual colors (in our case a lightsabre)
def retrieve_color_anomaly(pixel_color_values):
    color_map = {}
    for pxc in pixel_color_values:
        if pxc not in color_map:
            color_map[pxc] = 1
        else:
            color_map[pxc] += 1

    green_spectrum = dict(filter(lambda cm: cm[0] > 'f00000' and cm[0] < 'f9ffff', color_map.items()))

    if len(green_spectrum) > 25:
        write_to_serial("2")
    else:
        write_to_serial("0")


while True:
    pxcs = read_screen_color()
    retrieve_color_anomaly(pxcs)
    sleep(2)
