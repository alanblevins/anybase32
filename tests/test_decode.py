import pytest
import anybase32
from anybase32_samples import *


def test_crockford_modified():
    decoded = anybase32.decode(CROCKFORD_MODIFIED, anybase32.CROCKFORD_MODIFIED)
    assert(decoded == SAMPLE_TEXT)


def test_crockford():
    decoded = anybase32.decode(CROCKFORD, anybase32.CROCKFORD)
    assert(decoded == SAMPLE_TEXT)


def test_zbase32():
    decoded = anybase32.decode(ZBASE32, anybase32.ZBASE32)
    assert(decoded == SAMPLE_TEXT)


def test_rfc_3548():
    decoded = anybase32.decode(RFC_3548, anybase32.RFC_3548)
    assert(decoded == SAMPLE_TEXT)


def test_rfc_2938():
    decoded = anybase32.decode(RFC_2938, anybase32.RFC_2938)
    assert(decoded == SAMPLE_TEXT)


def test_rfc_46488():
    decoded = anybase32.decode(RFC_4648, anybase32.RFC_4648)
    assert(decoded == SAMPLE_TEXT)


def test_arbitrary():
    decoded = anybase32.decode(ARBITRARY, ARBITRARY_ALPHABET)
    assert(decoded == SAMPLE_TEXT)


def test_too_short_alphabet():
    with pytest.raises(ValueError) as e:
        anybase32.decode(RFC_3548, TOO_SHORT_ALPHABET)
    assert("Invalid base32 alphabet" in str(e))


def test_too_long_alphabet():
    with pytest.raises(ValueError) as e:
        anybase32.decode(RFC_3548, TOO_LONG_ALPHABET)
    assert("Invalid base32 alphabet" in str(e))


def test_repeat_character_alphabet():
    with pytest.raises(ValueError) as e:
        anybase32.decode(RFC_3548, REPEAT_CHARACTER_ALPHABET)
    assert("Invalid base32 alphabet" in str(e))


def test_binary():
    with open("tests/icon.png", "rb") as icon_file:
        icon_bytes = icon_file.read()
    decoded = anybase32.decode(ICON_ZBASE32, anybase32.ZBASE32)
    assert(decoded == icon_bytes)


def test_wrong_alphabet():
    with pytest.raises(TypeError) as e:
        anybase32.decode(RFC_3548, anybase32.NIGHTMARE)
    assert("Non-base32 digit found" in str(e))
