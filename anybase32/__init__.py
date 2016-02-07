"""Encode and decode base32 strings using arbitrary alphabets"""

import base64
import string

# Define known alphabets for convenience
RFC_3548 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
RFC_4648 = RFC_3548
RFC_2938 = "0123456789ABCDEFGHIJKLMNOPQRSTVW"
CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
CROCKFORD_MODIFIED = "0123456789abcdefghjkmnpqrtuvwxyz"
ZBASE32 = "ybndrfg8ejkmcpqxot1uwisza345h769"
NIGHTMARE = "dDO0o1IiLl6bB8UuVvWwNnMmZz2S5s7T"


def validate_alphabet(alphabet):
    """Verify that a base32 alphabet is valid

    Args:
        alphabet (str): Ordered, case-sensitive encoding/decoding alphabet

    Raises:
        ValueError: if the alphabet is not valid
    """
    if len(set([i for i in alphabet])) != 32:
        raise ValueError("Invalid base32 alphabet")


def validate_encoded_data(data, alphabet):
    """Verify that an encoded input is valid for a given alphabet

    Args:
        data (str): base32 encoded string
        alphabet (str): Ordered, case-sensitive encoding alphabet

    Raises:
        TypeError: if the string has characters outside the alphabet
    """
    validate_alphabet(alphabet)
    data_set = set([i for i in data])
    alphabet_set = set([i for i in alphabet])

    if not data_set.issubset(alphabet_set):
        raise TypeError("Non-base32 digit found")


def encode(data, alphabet=None):
    """Encode a string into base32 using a designated alphabet

    Args:
        data (str): String to encode into base32
        alphabet (str): Ordered, case-sensitive encoding alphabet
            Default alphabet is RFC3548

    Returns:
        str: base-32 encoded string
    """
    validate_alphabet(alphabet or RFC_3548)

    encoded = base64.b32encode(data)
    encoded = encoded.rstrip('=')

    if alphabet is not None:
        translator = string.maketrans(RFC_3548, alphabet)
        encoded = encoded.translate(translator)

    return encoded


def decode(data, alphabet=None):
    """Decode a base32 string using a designated alphabet

    Args:
        data (str): String to decode from base32
        alphabet (str): Ordered, case-sensitive encoding alphabet
            Default alphabet is RFC3548

    Returns:
        str: Decoded string
    """
    validate_alphabet(alphabet or RFC_3548)
    validate_encoded_data(data, alphabet or RFC_3548)

    encoded = data
    if alphabet is not None:
        translator = string.maketrans(alphabet, RFC_3548)
        encoded = data.translate(translator)

    # base64 module / RFC3548 requires padding for decoding
    encoded += '=' * ((8 - len(data) % 8) % 8)

    return base64.b32decode(encoded)

