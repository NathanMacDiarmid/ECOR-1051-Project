# Submitted April 2, 2020
# Team 28:
# Nathan MacDiarmid 101098993
# Anita Ntomchukwu 101138391
# Sam Hurd 101146639
# Yahya Shah 101169280
# MILESTONE 3

# IMPORTS

from Cimpl import copy, get_color, set_color, Image, choose_file, load_image, create_color, show, get_height, get_width
from simple_Cimpl_filters import grayscale

# CONSTANTS

COLOURS = ['black', 'white', 'red', 'lime', 'blue',
           'yellow', 'cyan', 'magenta', 'gray']

RGB_VALUES = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0),
              (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
              (128, 128, 128)]


def _adjust_component(component: int) -> int:
    """
    Returns the midpoint of a red, green, or blue coordinate in
    it's respective quandrant.
    
    QUADRANT 1 -> 0 - 63
    midpoint -> 31
    
    QUADRANT 2 -> 64 - 127
    midpoint -> 95
    
    QUADRANT 3 -> 128 -191
    midpoint -> 159
    
    QUADRANT 4 -> 192 - 255
    midpoint -> 223
    
    >>> _adjust_component(77)
    31
    
    >>> _adjust_component(12)
    31
    
    >>> _adjust_component(188)
    159
    
    *written by Nathan MacDiarmid*
    """
    if component >= 0 and component <= 63:
        return 31
    elif component >= 64 and component <= 127:
        return 95
    elif component >= 128 and component <= 191:
        return 159
    elif component >= 192 and component <= 255:
        return 223

# DEFINITIONS

# // MILESTONE 1 \\

# RED FUNCTION


def red_channel(image: Image) -> Image:
    """Returns a copy of an image with only redscale pixels.
    
    *written by Sam Hurd*
    
    >>>red_channel(image)
    image with all pixels red
    """
    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        red = create_color(r, 0, 0)
        set_color(new_image, x, y, red)
    return new_image

# GREEN FUNCTION


def green_channel(file: Image) -> Image:
    """
    Returns a copy of the inputed image with only greenscale pixels.
    
    *written by Nathan MacDiarmid*
    
    >>>green_channel(image)
    image with all pixels green
    """
    image = copy(file)

    for x, y, (r, g, b) in image:
        green = create_color(0, g, 0)
        set_color(image, x, y, green)

    return image

# BLUE FUNCTION


def blue_channel(inpic) -> Image:
    """Returns a copy of the inputed image with only bluescale pixels.
    
    written by Yahya Shah
    
    >>>blue_channel(image)
    image with all pixels blue
    """
    pic = copy(inpic)
    for i, m, (r, g, b) in pic:
        blue = create_color(0, 0, b)
        set_color(pic, i, m, blue)
    return pic

# COMBINE FUNCTION


def combine(red_image: Image, green_image: Image, blue_image: Image) -> Image:
    """
    Returns a single image that is a combination
    of the three r, g, b values of the inputed images.
    
    written by: Anita Ntomchukwu
    
    >>>combine(red_image, green_image, blue_image)
    image that looks exactly like the image before being passed through the red,
    green and blue channel filters.
    """

    original_image1 = red_image
    original_image2 = green_image
    original_image3 = blue_image

    comb = copy(original_image1)

    for x, y, (r, g, b) in comb:

        red = get_color(original_image1, x, y)[0]
        green = get_color(original_image2, x, y)[1]
        blue = get_color(original_image3, x, y)[2]

        new_color = create_color(red, green, blue)
        set_color(comb, x, y, new_color)

    return comb

# // MILESTONE 2 \\

# TWO TONE FILTER


def two_tone(image: Image, colour1: str, colour2: str) -> Image:
    '''Returns a copy of inputted image with two different tones 
    based on user selection. 
    
    written by: Anita Ntomchukwu

    >>> two_tone(image, 'red', 'white')
    image with only red and white pixels
    '''

    two_tone_image = copy(image)

    for i in range(len(COLOURS)):
        if colour1 == COLOURS[i]:
            tone1 = RGB_VALUES[i]
            new_c1 = create_color(tone1[0], tone1[1], tone1[2])
        if colour2 == COLOURS[i]:
            tone2 = RGB_VALUES[i]
            new_c2 = create_color(tone2[0], tone2[1], tone2[2])

    for x, y, (r, g, b) in two_tone_image:
        brightness = (r + g + b) // 3
        if 0 <= brightness <= 127:
            set_color(two_tone_image, x, y, new_c1)
        elif 128 <= brightness <= 255:
            set_color(two_tone_image, x, y, new_c2)

    return two_tone_image

# THREE TONE FILTER


def three_tone(image: Image, colour1: str, colour2: str, colour3: str) -> Image:
    '''Returns a copy of an inputted image with three different tones
    based on user selection.
    
    written by: Anita Ntomchukwu

    >>> three_tone(image, 'gray', 'black', 'lime')
    image with only gray, black and lime pixels
    '''

    three_tone_image = copy(image)

    for i in range(len(COLOURS)):
        if colour1 == COLOURS[i]:
            tone1 = RGB_VALUES[i]
            new_c1 = create_color(tone1[0], tone1[1], tone1[2])
        if colour2 == COLOURS[i]:
            tone2 = RGB_VALUES[i]
            new_c2 = create_color(tone2[0], tone2[1], tone2[2])
        if colour3 == COLOURS[i]:
            tone3 = RGB_VALUES[i]
            new_c3 = create_color(tone3[0], tone3[1], tone3[2])

    for x, y, (r, g, b) in three_tone_image:
        brightness = (r + g + b) // 3
        if 0 <= brightness <= 84:
            set_color(three_tone_image, x, y, new_c1)
        elif 85 <= brightness <= 170:
            set_color(three_tone_image, x, y, new_c2)
        elif 171 <= brightness <= 255:
            set_color(three_tone_image, x, y, new_c3)

    return three_tone_image

# EXTREME CONTRAST


def extreme_contrast(inpic: Image) -> Image:
    """Returns a copy of the inputed image with all pixel values set to
    their maximum.
    
    Author: Yahya Shah
    
    >>>extreme_contrast(image)
    image with only black or white pixels
    """
    pic = copy(inpic)

    for i, m, (r, g, b) in inpic:
        if r < 128:
            r = 0
        else:
            r = 255

        if g < 128:
            g = 0
        else:
            g = 255

        if b < 128:
            b = 0
        else:
            b = 255

        newcol = create_color(r, g, b)
        set_color(pic, i, m, newcol)

    return pic

# SEPIA FILTER


def sepia(image: Image) -> Image:
    """Returns a copy of an image with a sepia filter.
    
    *Written by Sam Hurd*
    
    >>> sepia(image)
    image with grayscale and a yellow tint
    """
    pic = grayscale(copy(image))

    for x, y, (r, g, b) in pic:

        if r < 63:
            b = b * 0.9
            r = r * 1.1

        elif r <= 191:
            b = b * 0.85
            r = r * 1.15

        else:
            b = b * 0.93
            r = r * 1.08

        color = create_color(r, g, b)
        set_color(pic, x, y, color)

    return pic

# POSTERIZE FILTER


def posterize(image: Image) -> Image:
    """
    Returns a copy of an image with the posterize filter.
    
    *written by Nathan MacDiarmid*
    
    >>> posterize(image)
    image with middle points in four different quadrants
    """
    image = copy(image)

    for x, y, (r, g, b) in image:

        new_red = _adjust_component(r)
        new_green = _adjust_component(g)
        new_blue = _adjust_component(b)

        new_colour = create_color(new_red, new_green, new_blue)
        set_color(image, x, y, new_colour)

    return image

# EDGE DETECTION


def detect_edges(image: Image, threshold: float) -> Image:
    """Returns a copy of an image with the pixels changed to either black 
    or white based on the contrast of the pixel above or below based on 
    inputed threshold.
    
    *Written by Sam Hurd*
    
    >>>detect_edges(image, 5)
    """

    image = copy(image)
    height = get_height(image)
    width = get_width(image)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for x in range(0, width):
        set_color(image, x, height - 1, white)

    for y in range(0, height - 1):
        for x in range(0, width):
            r, g, b = get_color(image, x, y)
            brightness1 = (r + g + b) // 3
            r2, g2, b2 = get_color(image, x, y + 1)
            brightness2 = (r2 + g2 + b2) // 3
            contrast = abs(brightness1 - brightness2)

            if contrast >= threshold:
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)

    return image

# IMPROVED EDGE DETECTION


def detect_edges_better(img: Image, threshold: int) -> Image:
    """
    Returns a copy of an image with the pixels changed to either black 
    or white based on the contrast of the pixel above, below, or to the right
    based on the inputed threshold.
    
    Author: Anita Ntomchukwu
    
    >>>detect_edges(img, 5)
    """
    new_img = copy(img)
    height = get_height(img)
    width = get_width(img)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    set_color(new_img, width - 1, height - 1, white)

    for x in range(0, width):
        set_color(new_img, x, height - 1, white)

    for y in range(0, height - 1):
        for x in range(0, width):

            color1 = get_color(img, x, y)
            color2 = get_color(img, x, y + 1)
            brightness1 = (color1[0] + color1[1] + color1[2]) // 3
            brightness2 = (color2[0] + color2[1] + color2[2]) // 3

            difference1 = abs(brightness1 - brightness2)

            if difference1 > threshold:
                set_color(new_img, x, y, black)
            else:
                set_color(new_img, x, y, white)

    for y in range(0, height):
        for x in range(0, width - 1):

            color3 = get_color(img, x, y)
            color4 = get_color(img, x + 1, y)
            brightness3 = (color3[0] + color3[1] + color3[2]) // 3
            brightness4 = (color4[0] + color4[1] + color4[2]) // 3

            difference2 = abs(brightness3 - brightness4)

            if difference2 > threshold:
                set_color(new_img, x, y, black)
            else:
                set_color(new_img, x, y, white)

    return new_img

# VERTICAL FLIP


def flip_vertical(image: Image) -> Image:
    """
    Returns a copy of an image that is flipped along a vertical line.
    
    *written by Nathan MacDiarmid*
    
    >>>flip_vertical(image)
    image flipped on a vertical line down centre
    """
    image = copy(image)

    width = get_width(image)
    height = get_height(image)

    for y in range(height):
        for x in range(width // 2):
            col1 = get_color(image, (width - x - 1), y)
            col2 = get_color(image, x, y)
            set_color(image, x, y, col1)
            set_color(image, (width - x - 1), y, col2)

    return image

# HORIZONTAL FLIP


def flip_horizontal(inpic: Image) -> Image:
    """Returns a copy of an image that is flipped along a horizontal line.
    
    Author: Yahya Shah
    
    >>>flip_horizontal(image)
    image flipped on a horizontal line down centre
    """
    pic = copy(inpic)

    width = get_width(pic)
    height = get_height(pic)

    for y in range(height // 2):
        for x in range(width):
            colour1 = get_color(pic, x, (height - y - 1))
            colour2 = get_color(pic, x, y)
            set_color(pic, x, (height - y - 1), colour2)
            set_color(pic, x, y, colour1)

    return pic
