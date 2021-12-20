import pytest
import requests


class TestsPositiveForServer:
    @pytest.mark.parametrize("number", [0, 5, 10])
    def test_input_valid_numbers_with_answer_ok(self, number):
        response = requests.post('http://127.0.0.1:5000/', data={'test': number})
        assert response.status_code == 200, f"Wrong status code response: {response.status_code}"
        assert response.text == "Ok", f"Wrong response: {response.text}"

    @pytest.mark.parametrize("number", [-1, -50, -100])
    def test_input_valid_numbers_with_answer_too_small(self, number):
        response = requests.post('http://127.0.0.1:5000/', data={'test': number})
        assert response.status_code == 500, f"Wrong status code response: {response.status_code}"
        assert response.text.strip() == "Value is too small", f"Wrong response: {response.text}"

    @pytest.mark.parametrize("number", [11, 50, 100])
    def test_input_valid_numbers_with_answer_too_large(self, number):
        response = requests.post('http://127.0.0.1:5000/', data={'test': number})
        assert response.status_code == 502, f"Wrong status code response: {response.status_code}"
        assert response.text.strip() == "Value is too large", f"Wrong response: {response.text}"


class TestsNegativeForServer:
    def test_request_method_is_wrong(self):
        response = requests.get('http://127.0.0.1:5000/')
        assert response.status_code == 222, f"Wrong status code response: {response.status_code}"
        assert response.text.strip() == "I'm only postable", f"Wrong response: {response.text}"

    def test_input_wrong_key(self):
        response = requests.post('http://127.0.0.1:5000/', data={'test1': "5"})
        assert response.status_code == 501, f"Wrong status code response: {response.status_code}"
        assert response.text.strip() == "Non integer data passed in request form", f"Wrong response: {response.text}"

    def test_input_wrong_value(self):
        response = requests.post('http://127.0.0.1:5000/', data={'test': "k5"})
        assert response.status_code == 501, f"Wrong status code response: {response.status_code}"
        assert response.text.strip() == "Non integer data passed in request form", f"Wrong response: {response.text}"
