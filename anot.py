import os
# Параметры
output_dir = './annotations/airport1/'
os.makedirs(output_dir, exist_ok=True)

# Создание аннотаций для 5 изображений
for i in range(5):
    # Координаты центра прямоугольника
    row = 100  # y-координата центра
    col = 100 + i * 10  # x-координата центра
    with open(os.path.join(output_dir, f'{i+1:04d}-01-01-01-01-01.txt'), 'w') as f:
        f.write(f"{row} {col}\n")


# Параметры для аннотаций второго аэропорта
output_dir_annotations = './annotations/airport2/'
os.makedirs(output_dir_annotations, exist_ok=True)

# Создание аннотаций для 5 изображений второго аэропорта
for i in range(5):
    # Координаты центра прямоугольника
    row = 100  # y-координата центра
    col = 100 + i * 10  # x-координата центра
    with open(os.path.join(output_dir_annotations, f'{i+1:04d}-01-01-01-01-01.txt'), 'w') as f:
        f.write(f"{row} {col}\n")

import os

# Создание директории для моделей
output_folder = './models/'
os.makedirs(output_folder, exist_ok=True)

# Пример данных для сохранения
model_parameters = {
    'learning_rate': 0.0001,
    'batch_size': 256,
    'num_iterations': 3000,
    'max_epochs': 50,
    'early_stopping': 10,
}

# Сохранение параметров модели в файл
with open(os.path.join(output_folder, 'model_parameters.txt'), 'w') as f:
    for key, value in model_parameters.items():
        f.write(f"{key}: {value}\n")

print("Директория 'models' и файл 'model_parameters.txt' успешно созданы!")
