import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    if s == "Hello,World!":
        print("AC")
    else:
        print("WA")


if __name__ == '__main__':
    main()
