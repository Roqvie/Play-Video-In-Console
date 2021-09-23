import click
import cv2
import numpy as np
from PIL import Image

from transformer import get_ascii_from_frame


@click.command()
@click.option('--path', type=click.Path(exists=True))
@click.option('--symbols', type=str, default='.-"~:;/+*ox8#%@¶')
@click.option('--shape', nargs=2, type=int)
@click.option('--image-type', type=click.Choice(['grayscale', 'treshold'], case_sensitive=False))
@click.option('--treshold', default=None, type=click.IntRange(0, 255))
def transform(path, symbols, shape, image_type, treshold):
    
    with Image.open(path) as image:
        image = np.array(image)
        frame = cv2.resize(image, shape, interpolation=cv2.INTER_AREA)
        if image_type == 'grayscale':
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif image_type == 'treshold' and treshold is not None:
            _, image = cv2.threshold(frame, treshold, 255, cv2.THRESH_BINARY)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ascii = get_ascii_from_frame(image, symbols)

        print(ascii)


if __name__ == '__main__':
    transform()