import  sys     #For debug purposes
import  random
from collections import Counter

FILEPATH    = "../CreatedFile.txt"
FILENL      = 15 #createCylinder(->n)

def     convertLetter(text):
    tmp_str = ""

    for letter in text:
        if letter.isalpha() and ord(letter) <= 123:
            tmp_str += letter
    return (tmp_str)

def     mix():
    buf_str = ""

    while (len(buf_str) < 26):
        buf_char = chr(random.randint(0, 25) + 65)
        if buf_char not in buf_str:
            buf_str += buf_char
    return (buf_str)

def     createCylinder(file, n):
    file_ = open(file, "w")

    for i in range(0, n):
        file_.write(mix() + "\n")
    file_.close()

def     ft_getnewlinesnb(str_):
    count = 0

    for i in range(0, len(str_)):
        if (str_[i] == '\n'):
            count += 1
    return (count)

def     loadCylinder(file):
    content = open(file, "r").read()
    lines_dict = {}
    i = 0
    buf = ""

    for i in range(0, ft_getnewlinesnb(content)):
        for j in range(0, 26):
            buf += content[(i * 27) + j]
        lines_dict[i + 1] = buf
        buf = ""
    return (lines_dict)

def     keyOK(key ,n):
    for i in range(1, n+1):
        if i not in key:
            return (False)
    return (True)

def     createKey(n):
    tmp_str = ""
    while (n != 0):
        tmp_str += str(n)
        n -= 1
    return (''.join(random.sample(tmp_str,len(tmp_str))))

def     find(letter, alphabet):
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            return (i)

def     shift(i):
    return ((-1), ((i + 6) % 26))[(i <= 25 and i >= 0)]

def     cipherLetter(letter, alphabet):
    return (alphabet[shift(find(letter, alphabet))])

def     cipherText(cylinder, key, text):
    k = 1
    c = ''

    if len(cylinder) != len(key):
        return ('The key is invalid')
    text = convertLetter(text)
    for t in text:
        n = cipherLetter(t, cylinder.get(k))
        c += cylinder.get(k)[n + 1]
        k += 1
    return (c)

