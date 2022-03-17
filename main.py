from PIL import ImageGrab
from screeninfo import get_monitors
import matplotlib.pyplot as plt
import collections
import statistics

# snapshot a certain area of the screen and interpret pixel colors
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

    pm = ImageGrab.grab(bbox=(
        padding_w, padding_h, screen.width - padding_w, screen.height - padding_h))
    pm.show()
    return pixel_hex_values


# searches for bright or unusual colors (in our case a lightsabre)
def retrieve_color_anomaly(pixel_color_values):
    color_map = {}
    for pxc in pixel_color_values:
        if pxc not in color_map:
            color_map[pxc] = 1
        else:
            color_map[pxc]+=1

    # check for anomalies larger than the median
    # ignore color codes that are present < 10 times because it distorts the statistic too much
    median = statistics.median(filter(lambda cm: cm > 10, color_map.values()))
    #color_map = dict(filter(lambda cm: cm[1] > median, color_map.items()))
    color_map_sorted = collections.OrderedDict(sorted(color_map.items()))

    green_spectrum = dict(filter(lambda cm: cm[0] > 'f00000' and cm[0] < 'f9ffff', color_map.items()))

    print('a')

    #f50000 fbff00
pxcs = read_screen_color()
retrieve_color_anomaly(pxcs)