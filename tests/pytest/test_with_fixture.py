import pytest


# All print(...) are shown for failed tests only
@pytest.fixture
def do_before():
    print('do_before:before')


@pytest.fixture(autouse=True)
def do_before_each():
    print('do_before_each:before')


@pytest.fixture
def do_around():
    print('do_around:before')
    yield
    print('do_around:after')


def test_with_before_fixture(do_before):
    assert False


def test_with_around_fixture(do_around):
    assert False
