from solutions.task7_moveZeroes import moveZeroes


def test_move_zeroes_example():
    a = [0, 1, 0, 3, 12]
    nonzero_before = [x for x in a if x != 0]
    moveZeroes(a)
    nonzero_after = [x for x in a if x != 0]

    assert nonzero_after == nonzero_before
    assert a == [1, 3, 12, 0, 0]


def test_move_zeroes_all_zeroes():
    a = [0, 0, 0]
    moveZeroes(a)
    assert a == [0, 0, 0]


def test_move_zeroes_no_zeroes():
    a = [1, 2, 3]
    moveZeroes(a)
    assert a == [1, 2, 3]


def test_move_zeroes_counts_preserved():
    a = [5, 0, 5, 0, 2, 0]
    z = a.count(0)
    moveZeroes(a)
    assert a.count(0) == z
    assert a[-z:] == [0] * z