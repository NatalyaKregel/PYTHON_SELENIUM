import logging
import pytest
from apipage import RestAPI


def test_api_username(expected_username):
    logging.info('Authorization on the site with using an authorization token')
    api_client = RestAPI()

    token = api_client.login()
    received_username = api_client.get_username(token)
    assert received_username == expected_username, logging.exception(f'{expected_username} not found in list')


if __name__ == '__main__':
    pytest.main(['-vv'])


