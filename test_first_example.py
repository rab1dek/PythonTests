def is_adult(age: int) -> bool:
    if age >= 18:
        return True

def test_is_adult():
    assert is_adult(20)

def test_is_not_adult():
    assert not is_adult(17)