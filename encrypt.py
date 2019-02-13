import sys

msg = str(sys.argv[1])
n = sys.argv[2]
e = sys.argv[3]

# switch to ascii code
def get_ascii(message):
    ascii_ = list()
    for i in range(0, len(message)):
        ascii_.append(ord(message[i]))
    return ascii_

# crypter the message


def crypter(code_ascii, N, E):
    n=int(N)
    e=int(E)
    crypted = list()
    message = str()
    for i in range(0, len(code_ascii)):
        cry = int((code_ascii[i] ** e) % n)
        crypted.append(cry)
        message += str(cry)
    return crypted

print(crypter(get_ascii(msg),n,e))

sys.stdout.flush()