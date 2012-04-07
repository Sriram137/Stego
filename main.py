import Image, sys
def encode(filename, outputfile, message, key):
    f = Image.open(filename)
    size, content, message = f.size[0] * f.size[1], list(f.getdata())
    message = message + chr(00)
    used_b = set()
    cryp = key.__hash__() % size   #Initial Key
    for c in message:
        while (cryp in used_b):
            cryp = (cryp * cryp + 1 ) % size
        replacement = tuple( [ord(c)] + list(content[cryp])[1:])
        content[cryp] = replacement
        used_b.add(cryp)
    f.putdata(content)
    f.save(outputfile)
    print "Successfully encrypted to file %s" % outputfile

def decode(filename, key):
    f = Image.open(filename)
    size, content = f.size[0] * f.size[1], list(f.getdata())
    used_bytes = set()
    cryp = key.__hash__() % size
    message = []

    while ord('a') <= content[cryp][0] <= ord('z') or ord('A') <= content[cryp][0] <= ord('Z'):
        while(cryp in used_bytes):
            cryp = (cryp * cryp + 1 ) % size
        message.append(chr(content[cryp][0]))
        used_bytes.add(cryp)
    print  "Decrytped message using your key is:\n %s" % "".join(message[:-1])

def wrong_usage():
    print 'Wrong usage'
    print 'Usage for encoding  : python main.py -e Inputfile Outputfile Message Key'
    print 'Usage for dencoding : python main.py -e Inputfile Key'
    print 'Extensions must be provied for filenames'

if __name__ == '__main__':
    try:
        if sys.argv[1] not in ['-e', '-d']:
            wrong_usage()
        if sys.argv[1] == '-e':
            encode(*sys.argv[2:])
        if sys.argv[1] == '-d':
            decode(*sys.argv[2:])
    except IndexError:
        wrong_usage()
    except Exception as e:
        print e
        wrong_usage()
