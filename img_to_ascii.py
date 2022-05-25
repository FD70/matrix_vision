import grayscale
import numpy as np
import cv2
import os

GRAYSCALE_TYPE = grayscale.GRAYSCALE_TYPE
GRAYSCALE_LENGTH = grayscale.GRAYSCALE_LENGTH


# np.asf.mean() - усреднение
# np.full((3, 5), 7, dtype=int)

if __name__ == '__main__':
    print('img_to_ascii start`s')
    shape = (480, 640)
    stream = cv2.VideoCapture(0)


    while(stream.read()[0]):
        os.system('cls')
        frame = stream.read()[1]
        for i in range(shape[0]//10):
            stringa = ''
            for j in range(shape[1]//10):
                ii = i*10
                jj = j*10
                cheap = frame[ii:ii + 10, jj:jj + 10].mean()
                stringa += 2 * GRAYSCALE_TYPE[-int(cheap * GRAYSCALE_LENGTH / 255)]
            print(stringa)
        # time.sleep(0.2)
    # main()



