import pytest


@pytest.mark.parametrize('code', ['101', '202', '303', '407', '501'])
def test_status_codes(test_client, code):
    response_status_code = test_client.status_code_analyzer(
        test_client.get, code)
    assert response_status_code == 200


@pytest.mark.parametrize('element, expected_text', [('h1', '403 Forbidden')])
def test_text_for_defaut_url(test_client, element, expected_text):
    response_text = test_client.analyze_text(test_client.get, element)
    assert response_text == expected_text


@pytest.mark.parametrize('element,path,classname,expected', [
    ('h1', '407', 'text-center my-12', '407 Proxy Authentication Required')])
def test_text_for_407_code(test_client, element, expected, path, classname):
    response_text = test_client.analyze_text(
        test_client.get, element, path, classname)
    assert response_text == expected
