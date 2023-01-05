#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argumentLength = len(sys.argv) - 1
    sum = 0
    for i in range(argumentLength):
        sum += sys.argv[i + 1]
    print(f'{sum}')
