from src.pytest_structure_example.calc import add


def test_add():
    x = 1
    y = 2
    expected = 3
    actual = add(x, y)
    assert expected == actual
