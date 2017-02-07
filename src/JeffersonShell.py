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

def     ft_is_anagram(str1, str2):
    if (len(str1) != len(str2)):
        return (False)
    return (Counter(str1) == Counter(str2))

def     keyOK(key, n):
    tmp_str = ""
    while (n != 0):
        tmp_str += str(n)
        n -= 1
    return (ft_is_anagram(key, tmp_str))

def     createKey(n):
    tmp_str = ""
    while (n != 0):
        tmp_str += str(n)
        n -= 1
    return (''.join(random.sample(tmp_str,len(tmp_str))))

def     find(letter, alphabet):
    i = 0

    while (alphabet[i] != letter and i < len(alphabet)):
        i += 1
    return (i)

def     shift(i):
    return ((-1), ((i + 6) % 26))[(i <= 25 and i >= 0)]

def     cipherLetter(letter, alphabet):
    return (alphabet[shift(find(letter, alphabet))])

#def     cipherText(cylinder, key, text):
#    

print(mix())
#print(cipherLetter(sys.argv[2], sys.argv[3]))
