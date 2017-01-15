anybase32
=========

anybase32 is a tiny Python package for encoding and decoding base32 bytes
using arbitrary 32-character alphabets. Useful for working with non-standard
base32 data from third party sources.

Works great on Python2 and Python 3. Tested with:
- Python 2.7.9
- Python 3.3.2
- Python 3.6.0

Usage
-----

```python
from __future__ import print_function
import anybase32

arbitrary_alphabet = b"0123456789`~!@#$%^&*()-_=+[]{}\/"
sample_text = b"The **quick** brown fox jumps over the (lazy) dog!"

encoded = anybase32.encode(sample_text, arbitrary_alphabet)

print(encoded)

decoded = anybase32.decode(encoded, arbitrary_alphabet)

print(decoded)
```

```
`^(6`81`59=_`[~3@!)2(832#9__#]^0!+__%83`#)-_0{+0@}]6`{^0#^(6`818@^%_(\9941&6\++1

The **quick** brown fox jumps over the (lazy) dog!
```

Alphabets
---------

anybase32 defines the following alphabets for convenience:

* RFC_3548 = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
* RFC_4648 = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
* RFC_2938 = b"0123456789ABCDEFGHIJKLMNOPQRSTVW"
* CROCKFORD = b"0123456789ABCDEFGHJKMNPQRSTVWXYZ"
* CROCKFORD_MODIFIED = b"0123456789abcdefghjkmnpqrtuvwxyz"
* ZBASE32 = b"ybndrfg8ejkmcpqxot1uwisza345h769"

anybase32 also defines this alphabet for inconvenience:

* NIGHTMARE = b"dDO0o1IiLl6bB8UuVvWwNnMmZz2S5s7T"
 
```python
from __future__ import print_function
import anybase32

encoded = (
    b"ktwgkebkfjazk4mdpcinwednqjzzq5tyc3zzoedkqiszyh3yp75gkhtyqtwgkebeptozw6jjr"
    b"b1g633b"
)
    
decoded = anybase32.decode(encoded, anybase32.ZBASE32)

print(decoded)
```

```
The **quick** brown fox jumps over the (lazy) dog!
```
