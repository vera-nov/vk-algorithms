from solutions.task5_sortColors import sortColors


def test_sort_colors_example():
    a = [2, 0, 2, 1, 1, 0]
    sortColors(a)
    assert a == [0, 0, 1, 1, 2, 2]


def test_sort_colors_already_sorted():
    a = [0, 0, 1, 1, 2, 2]
    sortColors(a)
    assert a == [0, 0, 1, 1, 2, 2]


def test_sort_colors_all_same():
    a = [1, 1, 1]
    sortColors(a)
    assert a == [1, 1, 1]


def test_sort_colors_counts_preserved():
    a = [2, 2, 0, 1, 0, 2, 1, 0]
    c0, c1, c2 = a.count(0), a.count(1), a.count(2)
    sortColors(a)
    assert a == sorted(a)
    assert a.count(0) == c0
    assert a.count(1) == c1
    assert a.count(2) == c2