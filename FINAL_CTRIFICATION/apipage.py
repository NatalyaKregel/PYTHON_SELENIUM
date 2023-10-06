import yaml, requests
import logging


class RestAPI:
    def __init__(self):
        with open('testdata.yaml', 'r') as f:
            self.config = yaml.safe_load(f)

        self.url_login = self.config['url_login']
        self.url_profile = self.config['url_profile']
        self.session = requests.Session()


    def login(self, ErrorReceivingToken=None):
        logging.info('Getting login token')
        try:
            response = requests.post(self.url_login, data={"username": self.config['login'],
                                                           "password": self.config['pswd']})
            if response.status_code == 200:
                return response.json().get('token')
            else:
                logging.exception('error_message')
        except Exception:
            logging.exception('error_message')


    def get_username(self, token):
        logging.info('Receiving data from the server')
        try:
            url = self.url_profile
            headers = {"X-Auth-Token": token}
            response = self.session.get(url, headers=headers)
            return response.json()['username']
        except Exception:
            logging.exception('error_message')

