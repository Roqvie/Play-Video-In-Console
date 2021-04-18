import click
import transformer


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--symbols', default='.~=*&%@#')
def play(path, symbols):
    transformer.play(video=path, symbols=symbols)


if __name__ == '__main__':
    play()

