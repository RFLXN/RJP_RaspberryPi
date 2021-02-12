import picamera  # PiCamera Library


class PiCameraWrapper:
    __camera = None

    def __init__(self):
        self.__camera = picamera.PiCamera()

    # function : capture PiCamera
    def capture_image(self, image_file_name):
        self.__camera.capture(image_file_name)
