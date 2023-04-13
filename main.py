import os
from PIL import Image, ImageOps

def resize_image(image_path, output_path, new_size):
    image = Image.open(image_path)
    width, height = image.size
    bg_color = image.getpixel((0, 0))

    padded_image = Image.new(image.mode, new_size, bg_color)
    padded_image.paste(image, ((new_size[0] - width) // 2, (new_size[1] - height) // 2))

    padded_image.save(output_path)

def process_images(input_folder, output_folder, new_size):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(input_path, output_path, new_size)

if __name__ == '__main__':
    input_folder = 'C:\img-resizer-2023'
    output_folder = 'C:\img-resizer-2023/newSize'
    new_size = (4500, 5400)

    process_images(input_folder, output_folder, new_size)
