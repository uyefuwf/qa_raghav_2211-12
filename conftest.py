import os
import json
import pytest
import requests
from config import Base_URL

@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session, Base_URL

with open("data.json") as f:
    data = json.load(f)
@pytest.fixture(params=data["payload"])
def post_payload(request):
    return request.param
@pytest.fixture(params=data["put"])
def put_payload(request):
    return request.param

@pytest.fixture(params=data["delete"])
def delete_payload(request):
    return request.param


@pytest.fixture(params=data["get"])
def get_payload(request):
    return request.param