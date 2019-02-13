import sys

def removee(string):
    string =string.replace('['," ")
    string =string.replace(','," ")
    string =string.replace(']'," ")
    return string


encrypted = removee(sys.argv[1]).split()
n = int(sys.argv[2])
d = int(sys.argv[3])
def decrypter(crypt, n, d):
    decrypt = list()
    output = str()
    for i in range(0, len(crypt)):
        decry = int((int(crypt[i]) ** d) % n)
        output += chr(decry)
    print(output)

decrypter(encrypted,  n, d)
sys.stdout.flush()