import pytest
from datetime import datetime
from protocol import make_response


@pytest.fixture
def action():
    return 'some_action'

@pytest.fixture
def user():
    print('connected')
    return 'some_user'

@pytest.fixture
def time():
    return datetime.now().timestamp()

@pytest.fixture
def data():
    print('connected')
    return 'some another data'

@pytest.fixture
def code():
    return 200

@pytest.fixture
def valid_request(action, user, time):
    return {
        'action': action,
        'user': user,
        'time': time,
    }

@pytest.fixture
def assert_response(
    action, user, time,
    data, code
):
    return {
        'action': action,
        'user': user,
        'time': time,
        'data': data,
        'code': code
    }


def test_make_response(
    valid_request, code, data,
    assert_response
):
    response = make_response(valid_request, code, data)

    for name, value in response.items():
        if name != 'time':
            assert value == assert_response.get(name)
