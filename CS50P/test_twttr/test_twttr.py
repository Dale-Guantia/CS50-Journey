from twttr import shorten

def test_words():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"
    assert shorten("tWiTtEr") == "tWTtr"

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("!?.,") == "!?.,"
