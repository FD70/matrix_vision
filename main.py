#FIXME: 20526 raw version on img_to_ascii.py

import img_to_ascii
import keyboard
import numpy as np
import cv2
import os


# ---=== task-list ===---
# [+] Захват видео с веб-камеры
# [+] Преобразование видео в набор символов (преобразование каждого кадра (FPS))
# [-] Вывод преобразованного визуального ряда в отдельное окно

# [-] Добавить возможность изменять цвет фона, символов реалтайм

# захват видеопотока с вед-камеры
VID_VEBCAM_STREAM = cv2.VideoCapture(0)
#
VID_STREAM_OUTPUT_NAME = 'Goblin'
# # выходной поток видео после всех преобразований
# VID_STREAM_OUTPUT_CONVERTED = None
# размер выходного потока видео
VID_STREAM_OUTPUT_SHAPE = (480, 640)
#
# TEXT_COLOR = '#ffffff'
#
# BG_COLOR = '#000000'


#FIXME: вероятно, использовать либы для вывода инормации ч-з html разметку
def text_to_frame():
    return


# показывает отдельный стрим в окне
def show_stream(stream_name, input_stream):
    # success -> type == bool; должен указывать на успешность чтения фрейма со стрима
    success, output_frame = input_stream.read()
    cv2.imshow(stream_name, output_frame)
    # waitKey(0) - отразится 1 кадр; waitKey(1) - поток идет
    cv2.waitKey(1)

def main():
    # while (VID_VEBCAM_STREAM.read()[0]):
    #     show_stream(VID_STREAM_OUTPUT_NAME, VID_VEBCAM_STREAM)
    return


if __name__ == '__main__':
    print('[+] запуск из main.py')

    os.system('cls')
    while(VID_VEBCAM_STREAM.read()[0]):
        print(img_to_ascii.img_to_ascii(VID_VEBCAM_STREAM.read()[1]))
    # main()
