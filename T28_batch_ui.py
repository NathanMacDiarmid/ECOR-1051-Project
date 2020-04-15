# Submitted April 2, 2020
# Team 28:
# Nathan MacDiarmid 101098993
# Anita Ntomchukwu 101138391
# Sam Hurd 101146639
# Yahya Shah 101169280
# MILESTONE 3

# IMPORTS

from T28_image_filters import *
from Cimpl import *

# DEFINITIONS


def execute_filter(command: tuple) -> Image:
    """
    Returns an image with the filters applied that are found in the batch file.
    
    >>>execute_filter('image.jpg', 'test1.jpg', 'T')
    image.jpg is saved as test1.jpg with the sepia filter applied
    """
    input_filename, output_filename, filters = command

    if filters == 'X':
        image = extreme_contrast((input_filename))
        return image

    elif filters == 'T':
        image = sepia((input_filename))
        return image

    elif filters == 'P':
        image = posterize((input_filename))
        return image

    elif filters == 'V':
        image = flip_vertical((input_filename))
        return image

    elif filters == 'H':
        image = flip_horizontal((input_filename))
        return image

    elif filters == '2':
        col1 = 'yellow'
        col2 = 'cyan'
        image = two_tone((input_filename), col1, col2)
        return image

    elif filters == '3':
        col1 = 'yellow'
        col2 = 'magenta'
        col3 = 'cyan'
        image = three_tone((input_filename), col1, col2, col3)
        return image

    elif filters == 'E':
        image = detect_edges((input_filename), 10)
        return image

    elif filters == 'I':
        image = detect_edges_better((input_filename), 10)
        return image

# SCRIPTING


filename = input("Please input the name of the batch file: ")
batch_file = open(filename, 'r')
i = 0
count = len(open(filename).readlines())
newlist = [0] * count

for line in batch_file:
    newline = line.split()
    newlist[i] = tuple(newline)
    i += 1

for x in newlist:
    lenght = len(x)
    i = 2
    image = load_image(x[0])
    while i < lenght:
        image = execute_filter((image, x[1], x[i]))
        i += 1
    save_as(image, x[1])

batch_file.close()
