import subprocess
import os
import ctypes
import random
import logging


def main():
    logging.basicConfig(filename='image_puller.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    filepath = os.getcwd() + '/images/' + random.choice(os.listdir('images'))
    logging.info(filepath)
    if os.name == 'nt':  # Windows
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, filepath, 0)
    elif os.name == 'posix':  # Linux
        subprocess.run(f'gsettings set org.gnome.desktop.background picture-uri "{filepath}"', shell=True)
    logging.info('Background has been changed.')


if __name__ == '__main__':
    main()
