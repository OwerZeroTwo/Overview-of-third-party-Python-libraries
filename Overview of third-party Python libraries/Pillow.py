# Библиотека Pillow используется для обработки изображений в Python.

# Задача: Изменить размер изображения и сохранить его в другом формате.


from PIL import Image

image = Image.open('image.jpg')
image = image.resize((500, 500))  # resize the image to 300x300
image.save('resized_image.png', 'PNG')