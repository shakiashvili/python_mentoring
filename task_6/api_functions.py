from api_classes import CatsAnalyzer


uris = CatsAnalyzer('https://http.cat/status/')

codes = ['101', '202', '303', '407', '501']


def first_func():
    expected_result = '407 Proxy Authentication Required'
    for code in codes:
        response_status_code = uris.status_code_analyzer(uris.get, code)
        assert response_status_code == 200

        if code == '407':
            res = uris.analyze_text(uris.get, 'h1', code, 'text-center my-12')
            assert res == expected_result


def second_func():
    excepted_result = '403 Forbidden'
    response = uris.analyze_text(uris.get, 'h1')
    assert response == excepted_result



