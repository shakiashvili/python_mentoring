import pytest
from models.cats_analyzer import CatsAnalyzer


@pytest.mark.parametrize('endpoint', ['101', '202', '303', '407', '501'])
def test_status_codes(test_client: CatsAnalyzer, endpoint: str) -> None:
    '''Testing the status codes to be 200, Ok '''
    response_status_code = test_client.get_endpoint_status_code(endpoint)
    assert response_status_code == 200


@pytest.mark.parametrize('expected_text', [('403 Forbidden')])
def test_text_for_defaut_url(test_client: CatsAnalyzer,
                             expected_text: str) -> None:
    response_text = test_client.get_h1_text()
    assert response_text == expected_text


@pytest.mark.parametrize('endpoint, classname, expected_text', [
    ('407', 'text-center my-12', '407 Proxy Authentication Required')])
def test_407(test_client: CatsAnalyzer, endpoint: str, classname: str,
             expected_text: str) -> None:
    response_text = test_client.get_h1_text(path=endpoint, classname=classname)
    assert response_text == expected_text
