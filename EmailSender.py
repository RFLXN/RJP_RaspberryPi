import smtplib  # Libraries for E-Mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class EmailSender:
    __sender_addr = ""
    __sender_pw = ""

    # constructor
    def __init__(self, sender_addr, sender_pw):
        self.__sender_addr = sender_addr
        self.__sender_pw = sender_pw

    # method : send e-mail
    def send_email(self, receive_address, mime_message):
        smtp_name = "smtp.gmail.com"
        smtp_port = 587

        smtp = smtplib.SMTP(smtp_name, smtp_port)
        smtp.starttls()
        smtp.login(self.__sender_addr, self.__sender_pw)
        smtp.sendmail(self.__sender_addr, receive_address, mime_message.as_string())

        smtp.quit()

    # method : create MIMEMultipart for send e-mail
    def create_mime_message(self, receive_address, time_info, file_names):
        message = MIMEMultipart()

        message["Subject"] = "Someone Detected On Sensor : " + time_info
        message["From"] = self.__sender_addr
        message["To"] = receive_address

        message.attach(MIMEText("Someone Detected On Sensor : " + time_info))

        for file_name in file_names:
            with open("images/" + file_name, "rb") as image_file:
                message_file_buff = MIMEApplication(image_file.read())
                message_file_buff.add_header("Content-Disposition", "attachment", filename=file_name)
                message.attach(message_file_buff)

        return message
