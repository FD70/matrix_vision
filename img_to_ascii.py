import grayscale
import numpy as np
import cv2
import os

GRAYSCALE_TYPE = grayscale.GRAYSCALE_TYPE
GRAYSCALE_LENGTH = grayscale.GRAYSCALE_LENGTH


def img_to_ascii(frame: np.ndarray):
    shape = frame.shape
    txt_out = ""
    for i in range(shape[0] // 10):
        one_line = ''
        for j in range(shape[1] // 10):
            ii = i * 10
            jj = j * 10
            cheap = frame[ii:ii + 10, jj:jj + 10].mean() # np.asf.mean() - усреднение
            one_line += 2 * GRAYSCALE_TYPE[-int(cheap * GRAYSCALE_LENGTH / 255)]
        txt_out += one_line[::-1] + "\n"
    return txt_out


if __name__ == '__main__':
    print('img_to_ascii start`s')

    stream = cv2.VideoCapture(0)

    while (stream.read()[0]):
        os.system('cls')
        print(img_to_ascii(stream.read()[1]))
        # img_to_ascii(stream.read()[1])
        # time.sleep(0.2)
