# Testing user endpoints.
import requests
import json

# Configurate test.
url: str = "http://127.0.0.1:5000"


def test_signup_user():
    data = {
        "name": "Afonso Medeiros",
        "email": "afonso@afonso.com",
        "password": "123456"
    }
    req = requests.post(f"{url}/user/new", json=data)
    status = req.status_code
    assert status == 200


def test_signup_professional():
    data = {
        "name": "Afonso Médico",
        "email": "afonso@medico.com",
        "password": "123456",
        "profession": "Psicologo"
    }
    req = requests.post(f"{url}/professional/new", json=data)
    status = req.status_code
    assert status == 200