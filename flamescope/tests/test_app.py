from flamescope import app as fapp
import pytest
from flask import url_for

from flamescope.util import stack

@pytest.fixture
def app():
    return fapp.APP

def test_app(app):
    assert app is not None

def test_list_stacks(client):
    assert client.get(url_for('stack.get_list')).status_code == 200


def test_get_stack_list():
    stacks = stack.get_stack_list()
    assert len(stacks) == 7
