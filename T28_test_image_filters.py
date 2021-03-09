# Submitted on March 26, 2020
# Team 28:
# Nahtan MacDiarmid
# Anita Ntomchukwu 101138391
# Sam Hurd 101146639
# Yahya Shah 101169280
# MILESTONE 2

# IMPORTS

from Cimpl import create_image, create_color, set_color, get_color
import T28_image_filters as T
from test_grayscale import check_equal

# DEFINITIONS

# // MILESTONE 1 \\

# RED TEST


def test_red() -> None:
    '''A test function for the red_channel filter.

    *written by Sam Hurd*
    
    >>>test_red()
    '''
    print('=============================')
    print('      TESTING RED FILTER     ')
    print('=============================')

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(255, 0, 0))
    set_color(original, 2, 0, create_color(0, 255, 0))
    set_color(original, 3, 0, create_color(0, 0, 255))
    set_color(original, 4, 0, create_color(127, 127, 127))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(255, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 4, 0, create_color(127, 0, 0))
    set_color(expected, 5, 0, create_color(255, 0, 0))

    red = T.red_channel(original)
    for x, y, col in red:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# GREEN TEST


def test_green() -> None:
    '''A test function for the green_channel filter.
    
    written by Nathan MacDiarmid.

    >>>test_green()
    '''
    print('=============================')
    print('     TESTING GREEN FILTER    ')
    print('=============================')

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(255, 0, 0))
    set_color(original, 2, 0, create_color(0, 255, 0))
    set_color(original, 3, 0, create_color(0, 0, 255))
    set_color(original, 4, 0, create_color(127, 127, 127))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 255, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 4, 0, create_color(0, 127, 0))
    set_color(expected, 5, 0, create_color(0, 255, 0))

    greenscale = T.green_channel(original)
    for x, y, col in greenscale:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# BLUE TEST


def test_blue() -> None:
    '''A test function for the blue_channel filter.
    
    written by Yahya Shah.

    >>>test_blue()
    '''
    print('=============================')
    print('     TESTING BLUE FILTER     ')
    print('=============================')

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(255, 0, 0))
    set_color(original, 2, 0, create_color(0, 255, 0))
    set_color(original, 3, 0, create_color(0, 0, 255))
    set_color(original, 4, 0, create_color(127, 127, 127))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 255))
    set_color(expected, 4, 0, create_color(0, 0, 127))
    set_color(expected, 5, 0, create_color(0, 0, 255))

    bluescale = T.blue_channel(original)
    for x, y, col in bluescale:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# COMBINE TEST


def test_combine() -> None:
    '''A test function for the combine filter.
    
    written by Anita Ntomchukwu.

    >>>test_combine()
    '''
    print('=============================')
    print('      TESTING COMBINE        ')
    print('=============================')

    original1 = create_image(6, 1)
    set_color(original1, 0, 0, create_color(0, 0, 0))
    set_color(original1, 1, 0, create_color(255, 0, 0))
    set_color(original1, 2, 0, create_color(0, 0, 0))
    set_color(original1, 3, 0, create_color(0, 0, 0))
    set_color(original1, 4, 0, create_color(127, 0, 0))
    set_color(original1, 5, 0, create_color(255, 0, 0))

    original2 = create_image(6, 1)
    set_color(original2, 0, 0, create_color(0, 0, 0))
    set_color(original2, 1, 0, create_color(0, 0, 0))
    set_color(original2, 2, 0, create_color(0, 255, 0))
    set_color(original2, 3, 0, create_color(0, 0, 0))
    set_color(original2, 4, 0, create_color(0, 127, 0))
    set_color(original2, 5, 0, create_color(0, 255, 0))

    original3 = create_image(6, 1)
    set_color(original3, 0, 0, create_color(0, 0, 0))
    set_color(original3, 1, 0, create_color(0, 0, 0))
    set_color(original3, 2, 0, create_color(0, 0, 0))
    set_color(original3, 3, 0, create_color(0, 0, 255))
    set_color(original3, 4, 0, create_color(0, 0, 127))
    set_color(original3, 5, 0, create_color(0, 0, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(255, 0, 0))
    set_color(expected, 2, 0, create_color(0, 255, 0))
    set_color(expected, 3, 0, create_color(0, 0, 255))
    set_color(expected, 4, 0, create_color(127, 127, 127))
    set_color(expected, 5, 0, create_color(255, 255, 255))

    combined = T.combine(original1, original2, original3)
    for x, y, col in combined:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# // MILESTONE 2 \\

# TWO TONE TEST


def test_two_tone() -> None:
    '''A test function for the two_tone filter.
    
    Author: Yahya Shah

    >>>test_two_tone()
    '''

    print('=============================')
    print('       TESTING TWO TONE      ')
    print('=============================')

    print('=============================')
    print('            TEST 1           ')
    print('=============================')

    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(255, 0, 0))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(255, 255, 255))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(0, 0, 255))
    set_color(expected, 1, 0, create_color(0, 0, 255))
    set_color(expected, 2, 0, create_color(0, 0, 255))
    set_color(expected, 3, 0, create_color(255, 0, 0))

    two = T.two_tone(original, 'blue', 'red')
    for x, y, col in two:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

    print('=============================')
    print('            TEST 2           ')
    print('=============================')

    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(255, 0, 0))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(255, 255, 255))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(0, 255, 0))
    set_color(expected, 1, 0, create_color(0, 255, 0))
    set_color(expected, 2, 0, create_color(0, 255, 0))
    set_color(expected, 3, 0, create_color(0, 255, 255))

    two = T.two_tone(original, 'lime', 'cyan')
    for x, y, col in two:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

    print('=============================')
    print('            TEST 3           ')
    print('=============================')

    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(255, 0, 0))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(255, 255, 255))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(255, 0, 255))
    set_color(expected, 1, 0, create_color(255, 0, 255))
    set_color(expected, 2, 0, create_color(255, 0, 255))
    set_color(expected, 3, 0, create_color(128, 128, 128))

    two = T.two_tone(original, 'magenta', 'gray')
    for x, y, col in two:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# THREE TONE TEST


def test_three_tone() -> None:
    '''A test function for the three_tone filter.
    
    Author: Yahya Shah

    >>>test_three_tone()
    '''

    print('=============================')
    print('      TESTING THREE TONE     ')
    print('=============================')

    print('=============================')
    print('            TEST 1           ')
    print('=============================')

    original = create_image(3, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(127, 127, 127))
    set_color(original, 2, 0, create_color(255, 255, 255))

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(0, 0, 255))
    set_color(expected, 1, 0, create_color(255, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))

    two = T.three_tone(original, 'blue', 'red', 'black')
    for x, y, col in two:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

    print('=============================')
    print('            TEST 2           ')
    print('=============================')

    original = create_image(3, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(127, 127, 127))
    set_color(original, 2, 0, create_color(255, 255, 255))

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(0, 255, 0))
    set_color(expected, 1, 0, create_color(0, 255, 255))
    set_color(expected, 2, 0, create_color(255, 255, 0))

    two = T.three_tone(original, 'lime', 'cyan', 'yellow')
    for x, y, col in two:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

    print('=============================')
    print('            TEST 3           ')
    print('=============================')

    original = create_image(3, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(127, 127, 127))
    set_color(original, 2, 0, create_color(255, 255, 255))

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(255, 0, 255))
    set_color(expected, 1, 0, create_color(128, 128, 128))
    set_color(expected, 2, 0, create_color(255, 255, 255))

    two = T.three_tone(original, 'magenta', 'gray', 'white')
    for x, y, col in two:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# EXTREME CONTRAST TEST


def test_extreme_contrast() -> None:
    '''A test function for the extreme contrast filter.

    *written by Sam Hurd*
    
    >>>test_extreme_contrast()
    '''
    print('=============================')
    print('   TESTING EXTREME CONTRAST  ')
    print('=============================')

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(255, 127, 129))
    set_color(original, 2, 0, create_color(0, 255, 0))
    set_color(original, 3, 0, create_color(128, 128, 128))
    set_color(original, 4, 0, create_color(127, 127, 127))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(255, 0, 255))
    set_color(expected, 2, 0, create_color(0, 255, 0))
    set_color(expected, 3, 0, create_color(255, 255, 255))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(255, 255, 255))

    extreme_contrast_image = T.extreme_contrast(original)
    for x, y, col in extreme_contrast_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# SEPIA TEST


def test_sepia() -> None:
    """
    A test function for the sepia filter.
    
    *written by Nathan MacDiarmid*
    
    >>> test_sepia()
    """
    print('=============================')
    print('        TESTING SEPIA        ')
    print('=============================')

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(127, 127, 127))
    set_color(original, 2, 0, create_color(56, 66, 32))
    set_color(original, 3, 0, create_color(150, 177, 132))
    set_color(original, 4, 0, create_color(200, 199, 255))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(146, 127, 107))
    set_color(expected, 2, 0, create_color(56, 51, 45))
    set_color(expected, 3, 0, create_color(175, 153, 130))
    set_color(expected, 4, 0, create_color(235, 218, 202))
    set_color(expected, 5, 0, create_color(255, 255, 237))

    new_sepia = T.sepia(original)
    for x, y, col in new_sepia:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# POSTERIZE TEST


def test_posterize() -> None:
    """A test function for the posterize filter.

    Author: Anita Ntomchukwu

    >>>test_posterize()
    """

    print('=============================')
    print('      TESTING POSTERIZE      ')
    print('=============================')

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(72, 240, 0))
    set_color(original, 1, 0, create_color(80, 127, 255))
    set_color(original, 2, 0, create_color(255, 255, 255))
    set_color(original, 3, 0, create_color(117, 111, 123))
    set_color(original, 4, 0, create_color(33, 72, 66))
    set_color(original, 5, 0, create_color(202, 152, 247))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(95, 223, 31))
    set_color(expected, 1, 0, create_color(95, 95, 223))
    set_color(expected, 2, 0, create_color(223, 223, 223))
    set_color(expected, 3, 0, create_color(95, 95, 95))
    set_color(expected, 4, 0, create_color(31, 95, 95))
    set_color(expected, 5, 0, create_color(223, 159, 223))

    posterize_image = T.posterize(original)
    for x, y, col in posterize_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# EDGE DETECTION TEST


def test_detect_edges() -> None:
    """A test function for the detect_edges filter.
    
    Author: Anita Ntomchukwu
    
    >>>test_detect_edges()
    """

    print('=============================')
    print('    TESTING EDGE DETECTION   ')
    print('=============================')

    original = create_image(1, 6)
    set_color(original, 0, 0, create_color(23, 34, 26))
    set_color(original, 0, 1, create_color(36, 52, 21))
    set_color(original, 0, 2, create_color(16, 10, 52))
    set_color(original, 0, 3, create_color(96, 79, 42))
    set_color(original, 0, 4, create_color(127, 225, 255))
    set_color(original, 0, 5, create_color(80, 200, 160))

    expected = create_image(1, 6)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 0, 2, create_color(0, 0, 0))
    set_color(expected, 0, 3, create_color(0, 0, 0))
    set_color(expected, 0, 4, create_color(0, 0, 0))
    set_color(expected, 0, 5, create_color(255, 255, 255))

    detect_edges_image = T.detect_edges(original, 5)
    for x, y, col in detect_edges_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# IMPROVED EDGE DETECTION TEST


def test_detect_edges_better() -> None:
    '''A test function for the detect edges better filter.

    *written by Sam Hurd*
    
    >>>test_detect_edges_better()
    '''

    print('===============================')
    print('TESTING IMPROVED EDGE DETECTION')
    print('===============================')

    print('===============================')
    print('            TEST 1             ')
    print('===============================')

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(255, 127, 129))
    set_color(original, 2, 0, create_color(0, 255, 0))
    set_color(original, 3, 0, create_color(128, 128, 128))
    set_color(original, 4, 0, create_color(127, 127, 127))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(255, 255, 255))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(255, 255, 255))

    detect_edges_better_image = T.detect_edges_better(original, 5)
    for x, y, col in detect_edges_better_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

    print('===============================')
    print('            TEST 2             ')
    print('===============================')

    original2 = create_image(1, 6)
    set_color(original2, 0, 0, create_color(0, 0, 0))
    set_color(original2, 0, 1, create_color(255, 127, 129))
    set_color(original2, 0, 2, create_color(0, 255, 0))
    set_color(original2, 0, 3, create_color(128, 128, 128))
    set_color(original2, 0, 4, create_color(127, 127, 127))
    set_color(original2, 0, 5, create_color(255, 255, 255))

    expected2 = create_image(1, 6)
    set_color(expected2, 0, 0, create_color(0, 0, 0))
    set_color(expected2, 0, 1, create_color(0, 0, 0))
    set_color(expected2, 0, 2, create_color(0, 0, 0))
    set_color(expected2, 0, 3, create_color(255, 255, 255))
    set_color(expected2, 0, 4, create_color(0, 0, 0))
    set_color(expected2, 0, 5, create_color(255, 255, 255))

    detect_edges_better_image = T.detect_edges_better(original2, 5)
    for x, y, col in detect_edges_better_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected2, x, y))

# VERTICAL FLIP TEST


def test_vertical() -> None:
    """
    A test for the flip_vertical filter.
    
    Author: Yahya Shah
    
    >>> test_vertical()
    """
    print('=============================')
    print('       TESTING VERTICAL      ')
    print('=============================')

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(127, 127, 127))
    set_color(original, 2, 0, create_color(56, 66, 32))
    set_color(original, 3, 0, create_color(150, 177, 132))
    set_color(original, 4, 0, create_color(200, 199, 255))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(200, 199, 255))
    set_color(expected, 2, 0, create_color(150, 177, 132))
    set_color(expected, 3, 0, create_color(56, 66, 32))
    set_color(expected, 4, 0, create_color(127, 127, 127))
    set_color(expected, 5, 0, create_color(0, 0, 0))

    vert = T.flip_vertical(original)
    for x, y, col in vert:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# HORIZONTAL FLIP TEST


def test_horizontal() -> None:
    """
    A test for the flip_horizontal filter.
    
    *written by Nathan MacDiarmid*
    
    >>> test_horizontal()
    """
    print('=============================')
    print('      TESTING HORIZONTAL     ')
    print('=============================')

    original = create_image(1, 6)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(127, 127, 127))
    set_color(original, 0, 2, create_color(56, 66, 32))
    set_color(original, 0, 3, create_color(150, 177, 132))
    set_color(original, 0, 4, create_color(200, 199, 255))
    set_color(original, 0, 5, create_color(255, 255, 255))

    expected = create_image(1, 6)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 0, 1, create_color(200, 199, 255))
    set_color(expected, 0, 2, create_color(150, 177, 132))
    set_color(expected, 0, 3, create_color(56, 66, 32))
    set_color(expected, 0, 4, create_color(127, 127, 127))
    set_color(expected, 0, 5, create_color(0, 0, 0))

    new_horizontal = T.flip_horizontal(original)
    for x, y, col in new_horizontal:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# SCRIPTING

# // MILESTONE 1 \\


test_red()
test_green()
test_blue()
test_combine()

# // MILESTONE 2 \\

test_two_tone()
test_three_tone()
test_extreme_contrast()
test_sepia()
test_posterize()
test_detect_edges()
test_detect_edges_better()
test_vertical()
test_horizontal()
