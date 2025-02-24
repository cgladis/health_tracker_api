def test_get_health_score(test_client):
    response = test_client.get("/api/get_health_score/1")
    assert response.status_code == 200
    assert "health_score" in response.json()
