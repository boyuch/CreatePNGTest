"""
Library file for image building functions
Assume that the incoming filenames are "correct" in that
they have the entire desired path.

NOTE: for these, for now you can assume the images are to
be 512x512 and can build your formulae with that in mind.

on a few of these, there are image size parameters given
(which for now will be 512x512) and so you can try generating
images whose size is not predetermined/hardcoded.
"""
from PIL import Image
import csv
from math import sqrt

def build_an_image_example(img_fname):
    """
    sample code to build an image and save it as PNG
    """
    # create the image in memory
    my_image = Image.new('RGB', (512,512) )
    my_image_pixels = my_image.load()

    # get the image size
    image_x_size = my_image.size[0]
    image_y_size = my_image.size[1]

    # iterate over x and y to pick the pixel color
    for x in range(image_x_size):
        for y in range(image_y_size):
            # pick the pixel color as an RGB tuple
            pixel_color = ( 254, 127, 3)

            # set the color to the image
            my_image_pixels[x, y] = pixel_color

    # save the image
    print(f'saving {img_fname}')
    my_image.save(img_fname, 'png')


def build_image_yellow(img_fname, image_x_size=512, image_y_size=512):
    """
    create an image that is full yellow.
    Just yellow at every pixel
    """
    my_image = Image.new('RGB', (512,512) )
    my_image_pixels = my_image.load()
    image_x_size = my_image.size[0]
    image_y_size = my_image.size[1]
    for x in range(image_x_size):
        for y in range(image_y_size):
            pixel_color = (255,255,0)
            my_image_pixels[x, y] = pixel_color
    print(f'saving {img_fname}')
    my_image.save(img_fname, 'png')


def build_image_double_red_gradient(img_fname):
    """
    create an image that gradient scales from 0 (black) to 255 (full red)
    of red intensity
    from left to right.  And when it reaches 255, start over at 0
    and start another gradient from 0 to 255.
    """
    my_image = Image.new('RGB', (512,512) )
    my_image_pixels = my_image.load()
    image_x_size = my_image.size[0]
    image_y_size = my_image.size[1]
    for x in range(image_x_size):
        for y in range(image_y_size):
            pixel_color = (x % 256,0,0)
            my_image_pixels[x, y] = pixel_color
    print(f'saving {img_fname}')
    my_image.save(img_fname, 'png')


def build_image_single_red_gradient(img_fname):
    """
    create an image that gradient scales from 0 to 255 of red
    but 0 has to be the leftmost and 255 has to be the rightmost
    and the gradient scales smoothly across the 512 horizontal pixels.
    """
    my_image = Image.new('RGB', (512,512) )
    my_image_pixels = my_image.load()
    image_x_size = my_image.size[0]
    image_y_size = my_image.size[1]
    for x in range(image_x_size):
        for y in range(image_y_size):
            pixel_color = (int(x / 2),0,0)
            my_image_pixels[x, y] = pixel_color
    print(f'saving {img_fname}')
    my_image.save(img_fname, 'png')


def build_image_yellow_gradient_horizontal(img_fname):
    """
    create an image that gradient scales from 0 to 255 of yellow
    but 0 has to be the leftmost and 255 has to be the rightmost
    and the gradient scales smoothly across the 512 horizontal pixels.
    Similar to test_single_red_gradient except color yellow instead
    of red
    """
    my_image = Image.new('RGB', (512,512) )
    my_image_pixels = my_image.load()
    image_x_size = my_image.size[0]
    image_y_size = my_image.size[1]
    for x in range(image_x_size):
        for y in range(image_y_size):
            pixel_color = (int(x / 2),int(x / 2),0)
            my_image_pixels[x, y] = pixel_color
    print(f'saving {img_fname}')
    my_image.save(img_fname, 'png')

def build_image_cyan_gradient_diagonal(img_fname):
    """
    Create an image that gradient scales from 0 to 255 of cyan.
    but 0 is the upper left corner and 255 is the bottom right corner.
    You may think in terms of adding the x and y coordinates together.
    Consider what the value of x+y is at the top left and at the
    bottom right
    """
    my_image = Image.new('RGB', (512,512) )
    my_image_pixels = my_image.load()
    image_x_size = my_image.size[0]
    image_y_size = my_image.size[1]
    for x in range(image_x_size):
        for y in range(image_y_size):
            pixel_color = (0,int((x + y)/4), int((x + y)/4))
            my_image_pixels[x , y] = pixel_color
    print(f'saving {img_fname}')
    my_image.save(img_fname, 'png')

def build_image_green_gradient_diagonal_inverted(img_fname):
    """
    Create an image that gradient scales from 255 to 0 of green.
    This is similar to build_image_cyan_gradient_diagonal except
    green and the 255 is top left and 0 is bottom right.
    """
    pass

def build_image_red_bands_horizontal(img_fname):
    """
    alternating bands of red (255 of red) and black (0) that
    are horizontal.

    Each red horizontal bar is 10 pixels tall.
    Each black horizontal bare is also 10 pixels tall
    """
    pass

def build_image_blue_bands_vertical(img_fname):
    """
    alternating vertical bands of blue (255 of blue) and black (0)
    Each bar is 10 pixels wide.  Similar to build_image_red_bands_horizontal
    except vertical
    """
    pass

def build_image_plaid_blue_and_red(img_fname):
    """
    red horizontal bands and blue vertical bands combined/overlayed onto
    each other.
    """
    pass

def build_image_banding_with_gradient_red(img_fname):
    """
    The red banding, but with a left-to-right blue/green intensity gradient
    ie., a gradient from 0 to 255 that goes from left to right of CYAN (blue/green)
    """
    pass


def build_palette_dictionary(palette_fname):
    """
    read the palette fname (CSV) and populate the dictionary
    using the first columna s the key and the RGB intensities
    as the value (as a tuple).

    NOTE: Make sure to use integer values!

    return the dictionary
    """
    my_palette_dict = dict()
    with open (palette_fname) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            key = int(row[0])
            value = (int(row[1]),int(row[2]),int(row[3]))
            my_palette_dict[key] = value
    return my_palette_dict

def palette_calculation(x,y):
    x_squared = x**2
    y_squared = y**2
    third_step = abs(x_squared - y_squared)
    fourth_step = 2 * (x * y)
    fifth_step = third_step + fourth_step
    sixth_step = int(sqrt(fifth_step))
    final_result = int(sixth_step % 255)
    return final_result

def build_image_using_palette(img_fname, palette_dict):
    """
    TROPHY
    use the palette_dict as a dictionary to look up colors
    key is an int (0-354) and the value is a 3-tuple of RGB
    Red if first element, Green is 2nd element, Blue is 3rd element

    Use this dictionary to determine the color of each pixel
    as follow:
        take the x coordinate and square it
        take the y coordinate and square it
        subtract the y square from the x square then take the abs of it
        multiple the x coordinate and the y coordinate and then double it
        add those two together
        take the square root of that.Make sure this is an INT
        divide it by the palette_max+1 (355 in our case) and take the remainder.


        This is your value

    Now, using the value, find the RGB color in the palette.  Set the
    pixel to that color
    """
    my_image = Image.new('RGB', (512,512) )
    my_image_pixels = my_image.load()
    image_x_size = my_image.size[0]
    image_y_size = my_image.size[1]
    for x in range(image_x_size):
        for y in range(image_y_size):
            final_result = palette_calculation(x,y)
            pixel_color = palette_dict[final_result]
            my_image_pixels[x, y] = pixel_color
    print(f'saving {img_fname}')
    my_image.save(img_fname, 'png')
