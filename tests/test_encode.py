import pytest
import anybase32
from anybase32_samples import *


def test_crockford_modified():
    encoded = anybase32.encode(SAMPLE_TEXT, anybase32.CROCKFORD_MODIFIED)
    assert(encoded == CROCKFORD_MODIFIED)


def test_crockford():
    encoded = anybase32.encode(SAMPLE_TEXT, anybase32.CROCKFORD)
    assert(encoded == CROCKFORD)


def test_zbase32():
    encoded = anybase32.encode(SAMPLE_TEXT, anybase32.ZBASE32)
    assert(encoded == ZBASE32)


def test_rfc_3548():
    encoded = anybase32.encode(SAMPLE_TEXT, anybase32.RFC_3548)
    assert(encoded == RFC_3548)


def test_rfc_2938():
    encoded = anybase32.encode(SAMPLE_TEXT, anybase32.RFC_2938)
    assert(encoded == RFC_2938)


def test_rfc_46488():
    encoded = anybase32.encode(SAMPLE_TEXT, anybase32.RFC_4648)
    assert(encoded == RFC_4648)


def test_arbitrary():
    encoded = anybase32.encode(SAMPLE_TEXT, ARBITRARY_ALPHABET)
    assert(encoded == ARBITRARY)


def test_too_short_alphabet():
    with pytest.raises(ValueError) as e:
        anybase32.encode(SAMPLE_TEXT, TOO_SHORT_ALPHABET)
    assert("Invalid base32 alphabet" in str(e))


def test_too_long_alphabet():
    with pytest.raises(ValueError) as e:
        anybase32.encode(SAMPLE_TEXT, TOO_LONG_ALPHABET)
    assert("Invalid base32 alphabet" in str(e))


def test_repeat_character_alphabet():
    with pytest.raises(ValueError) as e:
        anybase32.encode(SAMPLE_TEXT, REPEAT_CHARACTER_ALPHABET)
    assert("Invalid base32 alphabet" in str(e))


def test_binary():
    with open("tests/icon.png", "rb") as icon_file:
        icon_bytes = icon_file.read()

    encoded = anybase32.encode(icon_bytes, anybase32.ZBASE32)
    assert(encoded == ICON_ZBASE32)


