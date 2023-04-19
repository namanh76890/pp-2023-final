import tkinter as tk
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image_resized = image.resize((width, height), Image.LANCZOS)
    return image_resized

def on_button_click():
    print("Button clicked!")


def load_image(image_path, width, height):
    resized_image = resize_image(image_path, width, height)

    # Create a PhotoImage object with the resized image data
    photo_image = ImageTk.PhotoImage(resized_image)

    # Return the PhotoImage object
    return photo_image


