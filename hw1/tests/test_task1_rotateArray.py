from solutions.task1_rotateArray import rotate


def test_rotate_example():
    a = [1, 2, 3, 4, 5, 6, 7]
    rotate(a, 3)
    assert a == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_k_zero():
    a = [1, 2, 3]
    rotate(a, 0)
    assert a == [1, 2, 3]


def test_rotate_k_multiple_of_n():
    a = [1, 2, 3]
    rotate(a, 3)
    assert a == [1, 2, 3]


def test_rotate_k_greater_than_n():
    a = [1, 2, 3, 4]
    rotate(a, 10)
    assert a == [3, 4, 1, 2]


def test_rotate_single_element():
    a = [67]
    rotate(a, 999)
    assert a == [67]