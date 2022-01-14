import json


def test_good_model_return(test_app):
    client = test_app.test_client()
    resp = client.get("/")
