# lines 3 through 8: ask the user for the name of the file to copy, and try to open it to read; terminate the program execution if the open fails; note: use the exit() function to stop program execution and to pass the completion code to the OS; any completion code other than 0 says that the program has encountered some problems; use the errno value to specify the nature of the issue;
# lines 9 through 15: repeat nearly the same action, but this time for the output file;
# line 17: prepare a piece of memory for transferring data from the source file to the target one; such a transfer area is often called a buffer, hence the name of the variable; the size of the buffer is arbitrary - in this case, we decided to use 64 kilobytes; technically, a larger buffer is faster at copying items, as a larger buffer means fewer I/O operations; actually, there is always a limit, the crossing of which renders no further improvements; test it yourself if you want.
# line 18: count the bytes copied - this is the counter and its initial value;
# line 20: try to fill the buffer for the very first time;
# line 21: as long as you get a non-zero number of bytes, repeat the same actions;
# line 22: write the buffer's contents to the output file (note: we've used a slice to limit the number of bytes being written, as write() always prefer to write the whole buffer)
# line 23: update the counter;
# line 24: read the next file chunk;
# lines 29 through 31: some final cleaning - the job is done.


from os import strerror

srcname = input("Source file name?: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)
dstname = input("Destination file name?: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create destination file: ", strerr(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create destination file: ", strerr(e.errno))
    exit(e.errno)

print(total, 'byte(s) succesfully written')
src.close()
dst.close()