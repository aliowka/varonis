import json
from sanic_app.app import app
from unittest import TestCase


class TestSanicApp(TestCase):

    def test_user_not_found(self):
        params = {'username': 'pikachu', 'password': 'pika'}
        request, response = app.test_client.post('/auth', json=params)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['reasons'], ['User not found.'])

    def test_password_incorrect(self):
        params = {'username': 'varonis', 'password': 'pika'}
        request, response = app.test_client.post('/auth', json=params)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['reasons'], ['Password is incorrect.'])

    def test_normalize(self):
        params = {'username': 'varonis', 'password': 'varonis'}
        request, response = app.test_client.post('/auth', json=params)
        self.assertEqual(response.status_code, 200)

        access_token = response.json['access_token']

        test_data = json.dumps([{"name": "device",
                                  "strVal": "IPhone",
                                  "metadata": "not interesting"},
                                 {"name": "isAuthorized",
                                    "boolVal": "false",
                                    "lastSeen": "not interesting"}])

        request, response = app.test_client.post(
            "/normalize",
            data=test_data,
            headers={"Authorization": "Bearer {}".format(access_token)})

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.body, "{'device': 'strVal', 'isAuthorized': 'boolVal'}")
