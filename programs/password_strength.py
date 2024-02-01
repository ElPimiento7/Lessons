import string


def password_strength(value: str) -> str:
    if len(value) < 8:
        return "Too Weak"
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue
    if count == 3:
        return "Very good"
    return "Weak" if count == 1 else "Good"


if __name__ == '__main__':
    assert password_strength("") == "Too Weak"
    assert password_strength("1234567") == "Too Weak"
    assert password_strength("asdfghj") == "Too Weak"
    assert password_strength("ASDFGHJ") == "Too Weak"
    assert password_strength("AqSF45G") == "Too Weak"
    assert password_strength("12345678") == "Weak"
    assert password_strength("12345678990") == "Weak"
    assert password_strength("asdfghjk") == "Weak"
    assert password_strength("asdfghjfsdf") == "Weak"
    assert password_strength("ASDFGHJK") == "Weak"
    assert password_strength("ASDFGHJKGSD") == "Weak"
    assert password_strength("1234qwer") == "Good"
    assert password_strength("1234qwegfr") == "Good"
    assert password_strength("1234QWER") == "Good"
    assert password_strength("1234QWERSFG") == "Good"
    assert password_strength("qwerQWER") == "Good"
    assert password_strength("qwerQWERDFS") == "Good"
    assert password_strength("123qazQAZ") == "Very Good"
    assert password_strength("123345563Zq") == "Very Good"
    assert password_strength("qwertzdsqQ4") == "Very Good"
    assert password_strength("WSWFQQDDSD6f") == "Very Good"
