
# python imports
import threading

# local imports
from publisher_subscriber.utils import publisher, subscriber
from publisher_subscriber import constants


class OTPSubscriber(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        response = subscriber(constants.OTP_CHANNEL)
        print(response)


class OTPPublisher(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        message = "Your otp is 12345"
        response = publisher(constants.OTP_CHANNEL, message)
        print(response)


class NotificationSubscriber(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        response = subscriber(constants.NOTIFICATION_CHANNEL)
        print(response)


class NotificationPublisher(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        message = "You have one new notification"
        response = publisher(constants.NOTIFICATION_CHANNEL, message)
        print(response)