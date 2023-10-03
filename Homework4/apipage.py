import yaml, requests
import logging


class RestAPI:
    def __init__(self):
        with open('testdata.yaml', 'r') as f:
            self.config = yaml.safe_load(f)

        self.url_login = self.config['address']
        self.url_posts = self.config['api_address']
        self.session = requests.Session()

    def login(self, ErrorReceivingToken=None):
        logging.info('Getting login tokens')
        try:
            response = requests.post(self.url_login, data={"username": self.config['login'],
                                                           "password": self.config['pswd']})
            if response.status_code == 200:
                return response.json().get("token")
            else:
                error_message = ErrorReceivingToken(response.status_code)
                logging.exception(error_message)
        except Exception:
            logging.exception('error_message')

    def create_post(self, token, data):
        logging.info('Send to the server')
        try:
            url = self.url_posts
            headers = {"X-Auth-Token": token}
            response = self.session.post(url, headers=headers, json=data)
            return response
        except Exception:
            logging.exception('error_message')

    def get_posts(self, token):
        logging.info('Receiving data from the server')
        try:
            url = self.url_posts
            headers = {"X-Auth-Token": token}
            response = self.session.get(url, headers=headers)
            return response.json()["data"]
        except Exception:
            logging.exception('error_message')
