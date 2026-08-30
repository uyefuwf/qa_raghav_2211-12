class TestDelete:

    def test_delete(self,api_client,delete_payload):
        session,base_url = api_client
        response = session.delete(f"{base_url}/Activities/{delete_payload['id']}")
        assert response.status_code == 200

    def test_delete_not_found(self,api_client,delete_payload):
        session,base_url = api_client
        response = session.get(f"{base_url}/Activities/{delete_payload['id']}")
        data = response.json()
        print(data)

