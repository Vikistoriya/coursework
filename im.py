import cv2
import numpy as np
import os

# Параметры
output_dir = './images/airport1/'
os.makedirs(output_dir, exist_ok=True)

# Создание 5 изображений
for i in range(5):
    # Создание пустого изображения
    img = np.zeros((200, 200, 3), dtype=np.uint8)

    # Рисование белого прямоугольника (самолет)
    start_point = (50 + i * 10, 80)
    end_point = (150 + i * 10, 120)
    color = (255, 255, 255)  # белый цвет
    thickness = -1  # заполненный прямоугольник
    cv2.rectangle(img, start_point, end_point, color, thickness)

    # Сохранение изображения
    cv2.imwrite(os.path.join(output_dir, f'{i+1:04d}_image.png'), img)

# Параметры для второго аэропорта
output_dir_images = './images/airport2/'
os.makedirs(output_dir_images, exist_ok=True)

# Создание 5 изображений для второго аэропорта
for i in range(5):
    # Создание пустого изображения
    img = np.zeros((200, 200, 3), dtype=np.uint8)

    # Рисование белого прямоугольника (самолет)
    start_point = (50 + i * 10, 80)
    end_point = (150 + i * 10, 120)
    color = (255, 255, 255)  # белый цвет
    thickness = -1  # заполненный прямоугольник
    cv2.rectangle(img, start_point, end_point, color, thickness)

    # Сохранение изображения
    cv2.imwrite(os.path.join(output_dir_images, f'{i+1:04d}_image.png'), img)