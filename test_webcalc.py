"""This module does tests"""

import pytest
from expecter import expect

from webcalc import app, mongo


@pytest.fixture
def pattern():
    with app.app_context():
        mongo.db.operations.drop()
        mongo.db.operations.insert(
            dict(
                name="x",
                pattern="{{ a * b }}"
            )
        )
@pytest.fixture
def client():
    return app.test_client()


def describe_index():

    def it_says_hello(client):
        response = client.get('/')

        expect(response.data).contains(b"Hello, world!")



        def from_db(client, pattern):
            response = client.get('/4/x/5')

            expect(response.data).contains(b"20")
