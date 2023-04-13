# Image Resizer

This Python script takes all images in a specified input folder, resizes them to 4500x5400 pixels, and saves the resized images in a specified output folder. If the original image is smaller than the target size, the script adds border pixels to maintain the aspect ratio, with the border color matching the color of the top-left pixel.

## Dependencies

The script requires the `Pillow` package, which can be installed using the following command:

bashCopy code

`pip install Pillow` 

## Usage

1.  Open the script in your favorite text editor or Python IDE.
2.  Replace `'path/to/input/folder'` with the path to the folder containing the images you want to resize.
3.  Replace `'path/to/output/folder'` with the path to the folder where the resized images should be saved. If the folder does not exist, the script will create it.
4.  Save the script and run it using a Python interpreter.

bashCopy code

`python image_resizer.py` 

## Supported Image Formats

The script supports the following image formats:

-   PNG
-   JPG / JPEG
-   BMP
-   GIF
-   TIFF

Please note that the script processes only files with the appropriate file extensions in the input folder. Any other files or subdirectories will be ignored.
