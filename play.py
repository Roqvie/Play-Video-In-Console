import click as click
import transformer


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--symbols', type=str, default='.-"~:;/+*ox8#%@¶')
@click.option('--shape', nargs=2, type=int)
@click.option('--image-type', type=click.Choice(['grayscale', 'treshold'], case_sensitive=False))
@click.option('--treshold', default=None, type=click.IntRange(0, 255))
def play(path, symbols, shape, image_type, treshold):
    transformer.play(video=path, symbols=symbols, wh=shape, image_type=image_type, treshold=treshold)


if __name__ == '__main__':
    play()

