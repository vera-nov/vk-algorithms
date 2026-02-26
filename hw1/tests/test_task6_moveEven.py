from solutions.task6_moveEven import moveEven


def test_move_even_example_order_of_evens_preserved():
    a = [3, 2, 4, 1, 11, 8, 9]
    evens_before = [x for x in a if x % 2 == 0]
    moveEven(a)
    evens_after = [x for x in a if x % 2 == 0]

    assert evens_after == evens_before
    first_odd = next((i for i, x in enumerate(a) if x % 2 != 0), len(a))
    assert all(x % 2 == 0 for x in a[:first_odd])


def test_move_even_no_evens():
    a = [1, 3, 5]
    moveEven(a)
    assert a == [1, 3, 5]


def test_move_even_all_evens():
    a = [2, 4, 6]
    moveEven(a)
    assert a == [2, 4, 6]


def test_move_even_mixed_negative():
    a = [-3, -2, -4, 5]
    evens_before = [x for x in a if x % 2 == 0]
    moveEven(a)
    evens_after = [x for x in a if x % 2 == 0]
    assert evens_after == evens_before