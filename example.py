import anybase32

data = "The **quick** brown fox jumps over the (lazy) dog!"

print "Crockford modified", anybase32.encode(data, anybase32.CROCKFORD_MODIFIED)
print "Crockford", anybase32.encode(data, anybase32.CROCKFORD)
print "Zbase32", anybase32.encode(data, anybase32.ZBASE32)
print "RFC 3548", anybase32.encode(data, anybase32.RFC_3548)
print "RFC 2938", anybase32.encode(data, anybase32.RFC_2938)
print "RFC 4648", anybase32.encode(data, anybase32.RFC_4648)
print "Nightmare", anybase32.encode(data, anybase32.NIGHTMARE)
enc = anybase32.encode(data, "0123456789`~!@#$%^&*()-_=+[]{}\/")
print "Arbitrary", enc
dec = anybase32.decode(enc, "0123456789`~!@#$%^&*()-_=+[]{}\/")
print dec

with open("tests/icon.png", "rb") as icon:
    icon_bytes = icon.read()

icon = anybase32.encode(icon_bytes, anybase32.ZBASE32)
while len(icon) > 74:
    print '"%s"' % icon[:74]
    icon = icon[74:]
