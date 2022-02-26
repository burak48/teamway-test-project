import responses
import requests
from responses import matchers


@responses.activate
def test_questions():
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
