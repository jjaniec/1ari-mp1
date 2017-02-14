import  sys     #For debug purposes
import  random

FILEPATH    = "../CreatedFile.txt"
FILENL      = 20 #createCylinder(->n)


def convertLetter(text):
    tmp_str = ""

    for letter in text:
        if letter.isalpha() and ord(letter) <= 123:
            tmp_str += letter
    return (tmp_str.upper())

def mix():
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    chain = ''
    for i in range(len(letters)):
        s = random.randint(0,len(letters)-1)
        chain += letters[s]
        letters.remove(letters[s])
    return chain

def createCylinder(file, n):
    file_ = open(file, "w")

    for i in range(0, n):
        file_.write(mix() + "\n")
    file_.close()

def ft_getnewlinesnb(str_):
    count = 0

    for i in range(0, len(str_)):
        if (str_[i] == '\n'):
            count += 1
    return (count)

def loadCylinder(file):
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

def keyOk(key, n):
    for i in range(1,n+1):
        if i not in key:
            return False
    return True


def createKey(n):
    lst = []
    key = []
    for num in range(1,n+1):
        lst += [num]
    for i in range(n):
        k = random.randint(0,len(lst)-1)
        key += [lst[k]]
        lst.remove(lst[k])
    return key

def find(letter, alphabet):
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            return i

def shift(i):
    i += 6
    i %= 26
    return i

def unshift(i):
    i -= 6
    i %= 26
    return i

def cipherLetter(letter, alphabet):
    i = find(letter,alphabet)
    i = shift(i)
    return i

def uncipherLetter(letter, alphabet):
    i = find(letter, alphabet)
    i = unshift(i)
    return i

def cipherText(cylinder, key, text):
    k = 0
    c = ''
    if len(cylinder) != len(key):
        return('The key is invalid')
    text = convertLetter(text)
    for t in text:
        n = cipherLetter(t,cylinder.get(key[k]))
        c += cylinder.get(key[k])[n]
        k += 1
    return c

def uncipherText(cylinder, key, text):
    k = 0
    c = ''
    if len(cylinder) != len(key):
        return ('The key is invalid')
    text = convertLetter(text)
    for t in text:
        n = uncipherLetter(t, cylinder.get(key[k]))
        c += cylinder.get(key[k])[n]
        k += 1
    return c

cylinder = loadCylinder(FILEPATH)
h = 'XHWNIVTGBMZREQMFIREA'
key = [7, 4, 19, 13, 17, 18, 12, 15, 16, 10, 11, 2, 5, 20, 9, 8, 1, 14, 6, 3]

#print(uncipherText(cylinder,key,h))
print(cylinder)


#createCylinder(FILEPATH, FILENL)
#print(createKey(FILENL))
