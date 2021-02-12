from multiprocessing import Process
import RPi.GPIO as GPIO
import time

from GetNow import get_now
from EmailSender import EmailSender
from Config import Config
from CaptureImage import PiCameraWrapper

# Setup GPIO for IR Sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

# Initialize PiCamera Object for Capture Image
PiCamera = PiCameraWrapper()

# Initialize Config Object for Load config.json
Config = Config()

# Initilaize Emailsender Object for Send E-Mail
EmailSender = EmailSender(Config.sender_address, Config.sender_password)


# function : create file name list by time string
def create_file_names(timestr, file_num):
    __file_names = []

    for i in range(1, file_num+1):
        __file_names.append(timestr + "_" + str(i) + ".jpg")

    return __file_names


# function : send e-mails
def sendMails(file_names):
    for receiver_addr in Config.receiver_list:
        print("[MIME] Send E-Mail to " + receiver_addr)
        mail = EmailSender.create_mime_message(receiver_addr, now, file_names)
        EmailSender.send_email(receiver_addr, mail)
        print("[MIME] Send Complete!")


# main
while True:
    if GPIO.input(18) == 0:     # When Sensor Detect Someone
        now = get_now()

        print(now + " : SOMEONE DETECTED IN SENSOR")
        capture_num = Config.capture_num                    # config.json -> captureNum
        capture_interval = Config.capture_interval_sec      # config.json -> captureIntervalSec

        file_names = create_file_names(now, capture_num)

        for file_name in file_names:                        # Capture Images as The Number of file_names.length
            PiCamera.capture_image("images/" + file_name)
            print("[PiCamera] Image Captured : " + file_name)
            time.sleep(capture_interval)

        # Create New Process for Send E-Mail
        process = Process(target=sendMails, args=(file_names,))

        # Start Process (Send E-Mails)
        process.start()

        print("Waiting 10 sec...")
        time.sleep(10)
