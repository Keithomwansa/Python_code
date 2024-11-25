try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # processing goes here
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)

#

from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # actual processing goes here
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))

##
from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))