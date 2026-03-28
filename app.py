# GUI dependencies — tkinter for the window, Pillow for icon generation
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    # Create a 64x64 blue square with a white "A" as a placeholder icon
    img = Image.new("RGB", (64, 64), color=(0, 120, 212))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((22, 20), "A", fill=(255, 255, 255), font=font)

    # Save the icon next to this file and return its path
    icon_path = os.path.join(os.path.dirname(__file__), "app_icon.ico")
    img.save(icon_path, format="ICO")
    return icon_path

def main():
    # Create the main application window
    window = tk.Tk()
    window.title("Hello World App")
    window.geometry("300x200")

    # Generate and set the window icon
    icon_path = create_icon()
    window.iconbitmap(icon_path)

    # Display "Hello World" centered in the window at size 12 font
    label = tk.Label(window, text="Hello World", font=("Arial", 12))
    label.pack(expand=True)

    # Toggle the label text between "Hello World" and "Hello Universe"
    def toggle_text():
        if label.cget("text") == "Hello World":
            label.config(text="Hello Universe")
        else:
            label.config(text="Hello World")

    # Button that triggers the text toggle when clicked
    button = tk.Button(window, text="Hello Reality", command=toggle_text)
    button.pack(pady=10)

    # Start the event loop — keeps the window open
    window.mainloop()

# Entry point — only runs when executed directly, not when imported
if __name__ == "__main__":
    main()
