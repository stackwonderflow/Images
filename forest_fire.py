"""
This program highlights fires in an image by identifying pixels
whose red intensity is more than INTENSITY_THRESHOLD times the
average of the red, green, and blue values at a pixel. Those
"sufficiently red" pixels are then highlighted in the image
and other pixels are turned grey, by setting the pixel red,
green, and blue values to be all the same average value.
"""

from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.0
DEFAULT_FILE = 'images/greenland-fire.png'

def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)
    # TODO: your code here
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) / 3
        if pixel.red >= average * INTENSITY_THRESHOLD:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
            pixel.red = luminosity
            pixel.green = luminosity
            pixel.blue = luminosity
    return image

def compute_luminosity(red, green, blue):
    """
    Calculates the luminosity of a pixel using NTSC formula
    to weight red, green, and blue values appropriately.
    """
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)
    
def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()