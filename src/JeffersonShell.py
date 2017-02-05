import  sys     #For debug purposes
import  random

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

    for i in range(0, 26):
        buf_str += chr(random.randint(0, 25) + 65)
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
    #print(lines_dict)
    return (lines_dict)

#createCylinder(FILEPATH, FILENL)
#loadCylinder(FILEPATH)
