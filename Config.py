import json # json library


# json.config loader class
class Config:
    sender_address = None
    sender_password = None
    receiver_list = None

    capture_num = None
    capture_interval_sec = None

    # constructor: load config.json and initialize config variable
    def __init__(self):
        with open("config.json", "r") as config_file:
            __config = json.load(config_file)

            # Config for SMTP (e-mail)
            self.sender_address = __config["senderAddress"]
            self.sender_password = __config["senderPassword"]
            self.receiver_list = __config["receiveAddressList"]

            # Config For Image Capture
            self.capture_num = __config["captureNum"]
            self.capture_interval_sec = __config["captureIntervalSec"]
