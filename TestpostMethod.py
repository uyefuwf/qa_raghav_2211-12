import pytest
import json
class TestPOST:
    def test_post(self, api_client,post_payload):
        session,base_url = api_client
        response = session.post(f"{base_url}/Activities",json=post_payload)
        assert response.status_code == 200 or response.status_code == 201
        data = response.json()
        print(data)
        assert data["id"] == post_payload["id"]
        assert data["title"] == post_payload["title"]

    def test_putt(self, api_client,put_payload):
        session,base_url = api_client
        response1 = session.put(f"{base_url}/Activities/{put_payload["id"]}",json=put_payload)
        assert response1.status_code == 200 or response1.status_code == 201
        data = response1.json()
        print(data)
        assert data["id"] == put_payload["id"]
