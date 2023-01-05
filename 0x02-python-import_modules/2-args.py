#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argumentLength = len(sys.argv)
    if argumentLength == 1:
        print("{} arguments.".format(argumentLength - 1))
        break
    elif argumentLength == 2:
        print("{} argument:".format(argumentLength - 1))
    else:
        print("{} arguments:".format(argumentLength - 1))
    for i in range(1: argumentLength):
        print(f'{i}: {sys.argv[i]}')
