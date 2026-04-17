from picamera2 import Picamera2
from PIL import Image
import time

def capture_photo(output_path):
    picam2 = Picamera2()
    config = picam2.create_still_configuration()
    picam2.configure(config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file(output_path)
    picam2.close()
