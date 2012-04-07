def return_size(filename = "red1.png"):
    f = open(filename,"rb")
    size = 0
    for x in f:
        for _ in x:
            size += 1
    return size

def encode(filename="red1.png", message='a', key='passwd'):
    size = return_size(filename)
    # First and last bytes are used for header info
    used_bytes = list(xrange(100)) + list(xrange(size-100, size))
    used_bytes = {x for x in used_bytes}

    # print used_bytes

    f = open(filename, "r")
    content = list(f.read())
    # print content
    f.close()
    cryp = key.__hash__() % size   #Initial Key
    for c in message:
        while (cryp in used_bytes):
            cryp = (cryp * cryp + 1 ) % size
            used_bytes.add(cryp)
        replacement = str(hex(ord(c)))[2:]
        content[cryp] = "/x%s" % replacement
        print content[cryp]
        print repr(content[cryp])

    # print cryp, size
    # print "".join(content)
    # print content

# encode(message="")
encode()
