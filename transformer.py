from multiprocessing import Process, Queue
import cv2
import click
import time
import sys
import os


def get_ascii_from_frame(image, ascii_symbols):
    """Function to make ASCII-symbols frame from opencv image"""

    rows, cols = image.shape
    ascii_frame = '\n'.join([ ''.join([ ascii_symbols[image[i, j] // (256 // len(ascii_symbols))] for j in range(cols) ]) for i in range(rows)])

    return ascii_frame


def print_frames(buff, fps, offset=0.0005):
    """Get generated frame from buffer every frame time"""

    frame = True
    while frame:
        start_time = time.time()
        time.sleep(1. / fps - offset)
        frame = buff.get()
        click.clear()
        print(f"{frame}\n")

        # Print frame statistics
        frame_time = time.time() - start_time
        print("\nFrame time:      {:.6f}".format(frame_time))


def play_video(video, symbols, wh, image_type, treshold):

    # Read video data and create buffer-queue for pre-generated frames
    video = cv2.VideoCapture(video)
    fps = video.get(cv2.CAP_PROP_FPS)
    w, _ = wh
    frames_buffer = Queue(maxsize=int(fps*5))
    renderer = Process(target=print_frames, args=(frames_buffer, fps,))
    renderer.start()


    while video.isOpened():
        # Image transforming and processing
        ret, frame = video.read()
        if frame is None:
            frames_buffer.put(None)
            sys.exit()
        frame = cv2.resize(frame, wh, interpolation=cv2.INTER_AREA)
        if image_type == 'grayscale':
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif image_type == 'treshold' and treshold is not None:
            _, image = cv2.threshold(frame, treshold, 255, cv2.THRESH_BINARY)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ascii_frame = get_ascii_from_frame(image, symbols)
        # Put generated frame to buffer
        frames_buffer.put(ascii_frame)


    renderer.join()
    input('Press any key for EXIT\n')
    sys.exit()


def play_sound(path):
    """Play audio with ffmpeg"""

    options = [
        '-vn',
        '-nodisp',
        '-nostats',
        '-autoexit',
    ]
    os.system(f'ffplay {" ".join(options)} {path[:-4]}.mp3')
