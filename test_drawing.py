from PIL import Image, ImageDraw
import glob
import os

# 3.1
def convert_images(source_extension, target_extension):
    # Находим все файлы с расширением source_extension
    files = glob.glob(f'*.{source_extension}')

    for file in files:
        # Открываем изображение
        image = Image.open(file)

        # Создаем новое имя файла с заменой расширения
        new_filename = os.path.splitext(file)[0] + f'.{target_extension}'

        # Конвертируем и сохраняем изображение в целевом формате
        image.save(new_filename, target_extension)

        print(f"Converted {file} to {new_filename}")

# Пример использования функции
source_ext = 'jpg'
target_ext = 'png'

convert_images(source_ext, target_ext)

# 3.2 Дополняем функцию
def convert_images(source_extension, target_extension):
    # Находим все файлы с расширением source_extension
    files = glob.glob(f'*.{source_extension}')

    for file in files:
        # Открываем изображение
        image = Image.open(file)

        # Создаем новое имя файла с заменой расширения
        new_filename = os.path.splitext(file)[0] + f'.{target_extension}'

        # Конвертируем и сохраняем изображение в целевом формате
        image.save(new_filename, target_extension)

        print(f"Converted {file} to {new_filename}")

        # Рисуем незаполненный квадрат и текст в центре изображения
        draw = ImageDraw.Draw(image)
        width, height = image.size
        square_size = min(width, height) // 2

        square_left = (width - square_size) // 2
        square_top = (height - square_size) // 2
        square_right = square_left + square_size
        square_bottom = square_top + square_size

        draw.rectangle((square_left, square_top, square_right, square_bottom), outline='black')

        text = "Hello,\nWorld!"
        font = ImageFont.truetype("arial.ttf", 20)
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2
        draw.text((text_x, text_y), text, fill='black', font=font)

        # Сохраняем изображение с нарисованным квадратом и текстом
        image.save(new_filename)

# Пример использования функции
source_ext = 'jpg'
target_ext = 'png'

convert_images(source_ext, target_ext)



