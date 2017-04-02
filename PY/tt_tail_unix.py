# Thumbtack
# Implement unix tail command. Assuming the file is really large
#
import sys
import os

def tail(path_to_file, n=10):
    bufsize = 8192

    lines = int(sys.argv[1])
    fname = sys.argv[2]
    fsize = os.stat(fname).st_size

    iter = 0
    with open(sys.argv[2]) as f:
        if bufsize > fsize:
            bufsize = fsize-1
        data = []
        while True:
            iter +=1
            f.seek(fsize-bufsize*iter)
            data.extend(f.readlines())
            if len(data) >= lines or f.tell() == 0:
                print(''.join(data[-lines:]))
                break

if __name__ == "__main__":
    tail("test.py")
