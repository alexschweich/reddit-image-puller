import subprocess
import os
import ctypes
import random


def main():
    filepath = os.getcwd() + '/images/' + random.choice(os.listdir('images'))
    if os.name == 'nt':  # Windows
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, filepath, 0)
    elif os.name == 'posix':  # Linux
        subprocess.run(f'gsettings set org.gnome.desktop.background picture-uri "{filepath}"', shell=True)


if __name__ == '__main__':
    main()
