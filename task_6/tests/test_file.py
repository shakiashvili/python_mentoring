import pytest
from models.cats_analyzer import CatsAnalyzer


@pytest.mark.parametrize('endpoint', ['101', '202', '303', '407', '501'])
def test_status_codes(test_client: CatsAnalyzer, endpoint: str) -> None:
    response_status_code = test_client.get_endpoint_status_code(endpoint)
    assert response_status_code == 200


@pytest.mark.parametrize('element, expected_text', [('h1', '403 Forbidden')])
def test_text_for_defaut_url(test_client: CatsAnalyzer, element: str,
                             expected_text: str) -> None:
    response_text = test_client.analyze_text(element)
    assert response_text == expected_text


@pytest.mark.parametrize('element,endpoint,classname,expected', [
    ('h1', '407', 'text-center my-12', '407 Proxy Authentication Required')])
def test_407_status_code(test_client: CatsAnalyzer, element: str,
                         expected: str, endpoint: str, classname: str) -> None:
    response_text = test_client.analyze_text(element, endpoint, classname)
    assert response_text == expected
