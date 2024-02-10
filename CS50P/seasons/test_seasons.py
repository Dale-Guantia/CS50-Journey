from seasons import convert_to_words

def test_convert_to_words():
    assert convert_to_words("525600") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_words("13001760") == "Thirteen million, one thousand, seven hundred sixty minutes"
