from os import strerror

try:
    fo = open('newtext.txt', 'wt')  # a new file (newtext.txt) is created
    for i in range(10):
        s = "line #" + str(i + 1) + "\n"
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
#
from os import strerror

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i + 1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))

#
