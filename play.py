import os
import os.path
import click
from multiprocessing import Process
import transformer


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--with-sound', is_flag=True)
@click.option('--symbols', type=str, default='.-"~:;/+*ox8#%@¶')
@click.option('--shape', nargs=2, type=int)
@click.option('--image-type', type=click.Choice(['grayscale', 'treshold'], case_sensitive=False))
@click.option('--treshold', default=None, type=click.IntRange(0, 255))
def play(path, with_sound, symbols, shape, image_type, treshold):

    video = Process(target=transformer.play_video, args=(path, symbols, shape, image_type, treshold, ))

    if with_sound:
        # Make mp3 file for audio
        if not os.path.exists(f'{path[:-4]}.mp3'):
            os.system(f'ffmpeg -i {path} {path[:-4]}.mp3')
        audio = Process(target=transformer.play_sound, args=(path,))
        audio.start()

    video.start()
    video.join()
    if with_sound:
        audio.join()


if __name__ == '__main__':
    play()

