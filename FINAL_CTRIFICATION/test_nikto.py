import logging
from BaseApp import WebServerEvaluation


def test_nikto_vulnerability(get_nikto_command, expected_result):
    logging.info('Check a site for vulnerabilities using a command utility lines')
    web_server_evaluator = WebServerEvaluation()
    received_text = web_server_evaluator.executing_nikto_command(get_nikto_command)
    assert expected_result in received_text, logging.exception(f'Error: {expected_result} not found')
