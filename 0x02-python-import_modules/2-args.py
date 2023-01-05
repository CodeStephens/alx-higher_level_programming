#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} arguments:".format(len(argv)))
    for i in range(len(argv)):
        if i == 0:
            continue
        else:
            print(f'{i}: {sys.argv[i]}')
