from escpos.printer import Serial
from PIL import Image

def print_photo(image_path):
    printer = Serial(
        devfile='/dev/serial0',
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=1,
        timeout=1
    )

    img = Image.open(image_path).convert("L")
    printer.image(img, impl="bitImageColumn")
    printer.cut()
