# Algorithm
# read fixed buffer size into data from end of file,
# count "\n", if > 10 or reaching the start, start output
# if <= 10, reset seek and read another buffer

import os, sys

def tail(lines, filename):
    buf = 3000
    fsize = os.stat(filename).st_size
    print(fsize)

    iter = 0
    with open(filename) as f:
        while True:
            f.seek(0)
            iter += 1
            print(iter, fsize - buf * iter)
            if fsize - buf * iter >= 0:
                f.seek(fsize - buf * iter)
                data = f.read()
                lines_in_data = data.count("\n")
                if lines_in_data > lines:
                    break
            else:
                data = f.read()
                break
    print(data)
    print("-------------")
    for line in data.split('\n')[-lines-1:-1]:
        print(line)

tail(int(sys.argv[1]), sys.argv[2])
