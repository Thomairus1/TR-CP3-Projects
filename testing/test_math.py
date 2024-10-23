from equations import(
    add,
    sub,
    mul,
    div
)

def test_add():
    assert add(2, 10) == 12
    assert add(3, 5) == 8
    assert add(4, 6) == 10

def test_sub():
    assert sub(10, 2) == 8
    assert sub(6, 3) == 3
    assert sub(2, 2) == 0

def test_mul():
    assert mul(10, 2) == 20
    assert mul(6, 3) == 18
    assert mul(2, 2) == 4

def test_div():
    assert div(10, 2) == 5
    assert div(6, 3) == 2
    assert div(2, 2) == 1