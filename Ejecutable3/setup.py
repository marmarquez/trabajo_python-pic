import sys
from cx_Freeze import setup, Executable

setup(
    name = "USB LED Interface",
    version = "1.0",
    description = "Interfaz para encender Led con PIC18F4550",
    executables = [Executable("usb-led.py", base = "Win32GUI")])