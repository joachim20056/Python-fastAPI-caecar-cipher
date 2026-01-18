from app.caesar import caesar_cipher

def test_basic_shift():
    assert caesar_cipher("abc", 1) == "bcd"

def test_wraparound():
    assert caesar_cipher("xyz") == "abc"

def test_preserves_case():
    assert caesar_cipher("AbC", 1) == "BcD"

def test_non_letters_unchanged():
    assert caesar_cipher("Hello, World!", 1) == "Ifmmp, Xpsme!"

def test_large_key():
    assert caesar_cipher("abc", 27) == "bcd"