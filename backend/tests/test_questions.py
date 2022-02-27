import responses
import requests
from responses import matchers


@responses.activate
def test_questions_200_case():
    url = "http://127.0.0.1:8000/api/v1/questions"
    params = {"question_id": "test_1"}
    responses.add(
        responses.Response(
            method='GET',
            url=url,
            match=[matchers.query_param_matcher(params)]
        )
    )

    resp = requests.get(url, params=params)
    assert resp.status_code == 200


@responses.activate
def test_questions_204_case():
    url = "http://127.0.0.1:8000/api/v1/questions"
    params = {"question_id": "4"}
    responses.add(
        responses.Response(
            method='GET',
            url=url,
            json="",
            status=204
        )
    )

    resp = requests.get(url, params=params)
    assert resp.status_code == 204


@responses.activate
def test_questions_400_case():
    url = "http://127.0.0.1:8000/api/v1/questions"
    params = {"question_id": "5"}
    responses.add(
        responses.Response(
            method='GET',
            url=url,
            json="",
            status=400
        )
    )

    resp = requests.get(url, params=params)
    assert resp.status_code == 400


@responses.activate
def test_questions_500_case():
    url = "http://127.0.0.1:8000/api/v1/questions"
    params = {"question_id": "6"}
    responses.add(
        responses.Response(
            method='GET',
            url=url,
            json="",
            status=500
        )
    )

    resp = requests.get(url, params=params)
    assert resp.status_code == 500
