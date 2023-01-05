#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir(hidden_4)
    argumentLength = len(sys.argv) - 1
    sum = 0
    for i in range(argumentLength):
        sum += int(sys.argv[i + 1])
    print(f'{sum}')
