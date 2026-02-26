from solutions.task4_sortArray01 import sortArray01


def is_sorted_01(a):
    seen_one = False
    for x in a:
        if x == 1:
            seen_one = True
        elif x == 0:
            if seen_one:
                return False
        else:
            return False 
    return True


def test_sort_01_example():
    a = [1, 0, 1, 0, 1, 0]
    sortArray01(a)
    assert is_sorted_01(a)
    assert a.count(0) == 3
    assert a.count(1) == 3


def test_sort_01_all_zeros():
    a = [0, 0, 0]
    sortArray01(a)
    assert a == [0, 0, 0]


def test_sort_01_all_ones():
    a = [1, 1, 1]
    sortArray01(a)
    assert a == [1, 1, 1]


def test_sort_01_single():
    a = [0]
    sortArray01(a)
    assert a == [0]


def test_sort_01_random_mix_counts_preserved():
    a = [1, 1, 0, 0, 1, 0, 1]
    before0 = a.count(0)
    before1 = a.count(1)
    sortArray01(a)
    assert is_sorted_01(a)
    assert a.count(0) == before0
    assert a.count(1) == before1