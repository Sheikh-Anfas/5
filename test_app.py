from app import greeting


def test_default_greeting():
    assert greeting("") == "Hello, world!"


def test_named_greeting():
    assert greeting("Ada") == "Hello, Ada!"


def test_whitespace_is_removed():
    assert greeting("  Ada  ") == "Hello, Ada!"
