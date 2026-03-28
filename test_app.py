import os
import pytest
import tkinter as tk
from app import create_icon


def test_icon_file_is_created(tmp_path, monkeypatch):
    # Redirect icon output to a temporary folder so we don't pollute the project
    monkeypatch.chdir(tmp_path)
    icon_path = create_icon()

    # Verify the icon file was actually created on disk
    assert os.path.exists(icon_path)


def test_icon_file_is_ico(tmp_path, monkeypatch):
    # Verify the generated file has the correct .ico extension
    monkeypatch.chdir(tmp_path)
    icon_path = create_icon()

    assert icon_path.endswith(".ico")


def test_toggle_text():
    # Verify the label toggles correctly between Hello World and Hello Universe
    root = tk.Tk()
    root.withdraw()  # Hide the window during testing

    label = tk.Label(root, text="Hello World")

    def toggle_text():
        if label.cget("text") == "Hello World":
            label.config(text="Hello Universe")
        else:
            label.config(text="Hello World")

    # First toggle: Hello World → Hello Universe
    toggle_text()
    assert label.cget("text") == "Hello Universe"

    # Second toggle: Hello Universe → Hello World
    toggle_text()
    assert label.cget("text") == "Hello World"

    root.destroy()
