import os
import os.path
import cv2
import click
import time
from datetime import datetime

def get_ascii_from_frame(image, ascii_symbols):

    rows, cols = image.shape
    ascii_frame = ''
    for i in range(rows):
        for j in range(cols):
            ascii_frame += ascii_symbols[image[i, j] // (256 // len(ascii_symbols))]
        ascii_frame += '\n'

    return ascii_frame



async def play(video, symbols):
    video = cv2.VideoCapture(video)
    fps = video.get(cv2.CAP_PROP_FPS)
    negative_offset, average = 0, 0
    while video.isOpened():
        start_time = datetime.now()

        ret, frame = video.read()
        frame = cv2.resize(frame, (80,30), interpolation=cv2.INTER_AREA)
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows, cols = gray_image.shape
        click.clear()
        print(get_ascii_from_frame(gray_image, symbols))
        print("{:.6f} ".format(abs(1. / fps - average)))

        offset = (datetime.now() - start_time).total_seconds()
        sleep = 1. / fps - offset + negative_offset
        negative_offset = 0
        print(sleep)

        if not sleep <= 0.:
            time.sleep(sleep)
        else:
            negative_offset = sleep
        average = (datetime.now() - start_time).total_seconds()

    video.release()

