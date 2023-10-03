import logging
import pytest
from apipage import RestAPI


def test_api_create_post(post_data, post_descriptions, create_post_restapi):
    logging.info(create_post_restapi)
    api_client = RestAPI()

    token = api_client.login()

    api_client.create_post(token, post_data)
    posts = api_client.get_posts(token)
    try:
        assert post_descriptions in [i["description"] for i in posts], f'{post_descriptions} не найдено в списке'
    except Exception as e:
        logging.exception(f'Тест не пройден. Исключением: {e}')
        raise


if __name__ == '__main__':
    pytest.main(['-vv'])
