import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    img = Image.new("RGB", (64, 64), color=(0, 120, 212))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((22, 20), "A", fill=(255, 255, 255), font=font)
    icon_path = os.path.join(os.path.dirname(__file__), "app_icon.ico")
    img.save(icon_path, format="ICO")
    return icon_path

def main():
    window = tk.Tk()
    window.title("Hello World App")
    window.geometry("300x200")

    icon_path = create_icon()
    window.iconbitmap(icon_path)

    label = tk.Label(window, text="Hello World", font=("Arial", 12))
    label.pack(expand=True)

    window.mainloop()

if __name__ == "__main__":
    main()
