#FIXME: 20525 still not ready

import keyboard
import cv2

"""
Чтобы не забыть, что нужно получить в итоге:
вспомним фильм "Матрица", так вот, там был эпизод,
где картинка отрисовывалась, будто все окружение - это набор
зеленых символов на темном ( черном ) фоне.
Нужно повторить нечто подобное.
"""

# ---=== task-list ===---
# [-] Захват видео с веб-камеры
# [-] Преобразование видео в набор символов (преобразование каждого кадра (FPS))
# [-] Вывод преобразованного визуального ряда в отдельное окно

# [-] Добавить возможность изменять цвет фона, символов реалтайм

VID_VEBCAM_STREAM = cv2.VideoCapture(0)
#
VID_STREAM_OUTPUT_NAME = 'Goblin'
# выходной поток видео после всех преобразований
VID_STREAM_OUTPUT_CONVERTED = None
# размер выходного потока видео
VID_STREAM_OUTPUT_SHAPE = (800, 450)
#
# TEXT_COLOR = '#ffffff'
#
# BG_COLOR = '#000000'


#FIXME:
def video_to_text():
    return


#FIXME:
def text_to_frame():
    return

# показывает отдельный стрим в окне
def show_stream(stream_name, input_stream):
    # success -> type == bool; должен указывать на успешность чтения фрейма со стрима
    success, output_frame = input_stream.read()
    cv2.imshow(stream_name, output_frame)
    # waitKey(0) - отразится 1 кадр; waitKey(1) - поток идет
    cv2.waitKey(1)


if __name__ == '__main__':
    print('[+] запуск из main.py')


while(VID_VEBCAM_STREAM.read()[0]):
    show_stream(VID_STREAM_OUTPUT_NAME, VID_VEBCAM_STREAM)
