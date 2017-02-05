import  sys     #For debug purposes
import  random

file = open("../CreatedFile.txt", "w")

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
    for i in range(0, n):
        file.write(mix() + "\n")
    file.close()

createCylinder(file, 25)
