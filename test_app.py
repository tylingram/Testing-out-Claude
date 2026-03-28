import os
import pytest
from app import create_icon, get_toggled_text


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
    # First toggle: Hello World → Hello Universe
    assert get_toggled_text("Hello World") == "Hello Universe"

    # Second toggle: Hello Universe → Hello World
    assert get_toggled_text("Hello Universe") == "Hello World"
