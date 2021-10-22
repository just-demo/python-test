import pytest


@pytest.mark.parametrize('a,b', [[1, 2], [3, 2]])
def test_with_parameters_array(a, b):
    assert a < b


@pytest.mark.parametrize('a,b', [(1, 2), (3, 2)])
def test_with_parameters_tuple(a, b):
    assert a < b


# produces [1, 3] x [2, 2] scenarios
@pytest.mark.parametrize('a', [1, 3])
@pytest.mark.parametrize('b', [2, 2])
def test_with_parameters_matrix(a, b):
    assert a < b
