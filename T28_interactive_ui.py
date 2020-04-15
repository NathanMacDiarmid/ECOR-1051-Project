# Submitted April 2, 2020
# Team 28:
# Nathan MacDiarmid 101098993
# Anita Ntomchukwu 101138391
# Sam Hurd 101146639
# Yahya Shah 101169280
# MILESTONE 3

# IMPORTS

from Cimpl import *
from T28_image_filters import *

# CONSTANTS

COLOURS = ['black', 'white', 'red', 'lime', 'blue',
           'yellow', 'cyan', 'magenta', 'gray']

FILTERS = {'2': two_tone, '3': three_tone, 'X': extreme_contrast, 'T': sepia,
           'P': posterize, 'E': detect_edges, 'I': detect_edges_better,
           'V': flip_vertical, 'H': flip_horizontal}

# DEFINITIONS


def initialize_ui() -> None:
    """
    Returns the user interface when called.
    """
    print('\nPLEASE CHOOSE AN OPTION\n')
    print('L)oad Image  S)ave-as')
    print('2)-tone  3)-tone  X)treme Contrast  T)int Sepia  P)osterize')
    print('E)dge Detection  I)mproved Edge Detection  V)ertical Flip  H)orizontal Flip')
    print('Q)uit')


def search_dict(n: str, pic: Image) -> Image:
    """
    Returns a loaded image with a specific filter applied.
    
    >>> search_dict('T', image)
    image with the sepia filter applied
    """

    if n == 'X' or n == 'T' or n == 'P' or n == 'V' or n == 'H':
        image = FILTERS[n](pic)
        show(image)
        return image

    elif n == '2':
        print('Please choose two colours')
        print(COLOURS)
        col1 = input(': ')
        col2 = input(': ')
        image = FILTERS[n](pic, col1, col2)
        show(image)
        return image

    elif n == '3':
        print('Please choose three colours')
        print(COLOURS)
        col1 = input(': ')
        col2 = input(': ')
        col3 = input(': ')
        image = FILTERS[n](pic, col1, col2, col3)
        show(image)
        return image

    elif n == 'E' or n == 'I':
        print('Please choose a threshold')
        thresh = int(input(': '))
        image = FILTERS[n](pic, thresh)
        show(image)
        return image

    return pic

# SCRIPTING


program = True
image = None

while program == True:

    initialize_ui()

    choice = input('\n: ')
    choice = choice.upper()

    if choice == 'L':
        image = copy(load_image(choose_file()))

    if choice != 'Q' and choice != 'L' and choice != 'S':

        if image == None:

            if choice in FILTERS.keys():
                print('No image loaded')

            else:
                print('No such command')

        elif choice not in FILTERS.keys():
            print('No such command')

        else:
            image = search_dict(choice, image)

    if choice == 'S':

        if image != None:
            print('MAKE SURE TO INCLUDE AN EXTENSION IN NAME (ex. .jpg, .png, etc.)')
            show(image)
            save_as(image)

        else:
            print('There is nothing to save')

    if choice == 'Q':
        program = False
