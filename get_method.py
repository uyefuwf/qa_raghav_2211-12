import pytest
class TestGetMethod:
    def test_get_method(self, api_client, get_payload):
        session,base_url= api_client
        response = session.get(f"{base_url}/Activities/{get_payload['id']}")
        assert response.status_code == 200
        assert "id" in response.json()
    @pytest.mark.parametrize("ic_resource_id", ["67frw2", "abx", "@"])
    def test_get_method_with_ic_params(self, api_client, ic_resource_id):
        session,base_url= api_client
        response2 = session.get(f"{base_url}/Activities/{ic_resource_id}")
        assert response2.status_code == 400, response2.status_code

