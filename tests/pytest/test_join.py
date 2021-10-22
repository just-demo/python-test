from testable.join import join


def test_join_int():
    assert join(1, 2, 3) == '123'


def test_join_str():
    assert join('1', '2', '3') == '123'


def test_join_mixed():
    assert join(1, '2', [3]) == '12[3]'
