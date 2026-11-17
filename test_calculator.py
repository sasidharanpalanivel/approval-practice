from calculator import add, clean_name


def test_add_two_numbers():
    assert add(2, 3) == 5


def test_add_negative_number():
    assert add(-1, 1) == 0


def test_clean_name_removes_spaces_and_fixes_capitals():
    assert clean_name("  sasidharan palanivel ") == "Sasidharan Palanivel"
