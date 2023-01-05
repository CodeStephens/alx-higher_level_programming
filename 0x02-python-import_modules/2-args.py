#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argumentLength = len(sys.argv)
    if argumentLength == 1:
        print("0 arguments.")
    elif argumentLength == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argumentLength - 1))
    for i in range(argumentLength - 1):
        print(f'{i + 1}: {sys.argv[i + 1]}')
