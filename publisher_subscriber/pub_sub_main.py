#!/usr/bin/python3
from publisher_subscriber import constants


class PubSubMain():

    def start_threading(self):

        publisher_classes = constants.CLASSES
        if publisher_classes:
            while True:
                for publisher_class in publisher_classes:
                    thread = publisher_class()
                    thread.start()