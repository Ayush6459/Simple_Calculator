from Calculator import add_num, sub_num


def test_calculator_to_add():
    assert add_num(5, 6) == 11


def test_calculator_to_sub():
    assert sub_num(6, 5) == 1
