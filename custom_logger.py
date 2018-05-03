import logging
from datetime import datetime
import json


class CustomLogger():

    def __init__(self):
        self.logger = logging.getLogger("master_app")
        self.app = "master_app"

    def log_info(self, request_id, message, http_method, api_path, data, app_name):
        
        logging.basicConfig(format='%(message)s', filename=self.app + '.log', level=logging.INFO)
        today = datetime.now()
        date_time = today.strftime("%d/%m/%Y-%H:%M:%S")

        if http_method.upper() == "GET":
            self.logger.info(app_name.upper() + " " + request_id + " " + date_time + " " + http_method.upper() + " " + api_path + " " + json.dumps(data) + " " + message)
        else:
            self.logger.info(app_name.upper() + " " + request_id + " " + date_time + " " + http_method.upper() + " " + api_path + " " + message)


    def log_debug(self, request_id, message, http_method, api_path, data, app_name):

        logging.basicConfig(format='%(message)s', filename=self.app + '.log', level=logging.DEBUG)
        today = datetime.now()
        date_time = today.strftime("%d/%m/%Y-%H:%M:%S")

        if http_method.upper() == "GET":
            self.logger.debug(app_name.upper() + " " + request_id + " " + date_time + " " + http_method.upper() + " " + api_path + " " + json.dumps(data) + " " + message)
        else:
            self.logger.debug(app_name.upper() + " " + request_id + " " + date_time + " " + http_method.upper() + " " + api_path + " " + message)


    def log_warning(self, request_id, message, http_method, api_path, data, app_name):
        
        logging.basicConfig(format='%(message)s', filename=self.app + '.log', level=logging.WARNING)
        today = datetime.now()
        date_time = today.strftime("%d/%m/%Y-%H:%M:%S")

        if http_method.upper() == "GET":
            self.logger.warning(app_name.upper() + " " + request_id + " " + date_time + " " + http_method.upper() + " " + api_path + " " + json.dumps(data) + " " + message)
        else:
            self.logger.warning(app_name.upper() + " " + request_id + " " + date_time + " " + http_method.upper() + " " + api_path + " " + message)


    def log_error(self, request_id, message, http_method, api_path, data, app_name):
        
        logging.basicConfig(format='%(message)s', filename=self.app + '.log', level=logging.ERROR)
        today = datetime.now()
        date_time = today.strftime("%d/%m/%Y-%H:%M:%S")

        if http_method.upper() == "GET":
            self.logger.error(app_name.upper() + " " + request_id + " " + date_time + " " + http_method.upper() + " " + api_path + " " + json.dumps(data) + " " + message)
        else:
            self.logger.error(app_name.upper() + " " + request_id + " " + date_time + " " + http_method.upper() + " " + api_path + " " + message)


class DatabaseCustomLogger():


    def __init__(self):
        self.logger = logging.getLogger("django.db.backends")
        self.app = "database"


    def database_logger(self, request_id):

        logging.basicConfig(format='[%(message)s]', filename=self.app + '.log')
        self.logger.setLevel(logging.DEBUG)
        # self.logger.addHandler(logging.StreamHandler())


class CustomFilter(logging.Filter):

    def filter(self, req_id=12):
        request_id = req_id
        print(request_id)
        return True


# %{WORD:name} %{NUMBER:id} %{DATESTAMP:date} %{WORD:httpmethod} %{URIPATHPARAM:request_url} %{WORD:message}
# notification 13 19/04/2018-02:06:21 GET /register message