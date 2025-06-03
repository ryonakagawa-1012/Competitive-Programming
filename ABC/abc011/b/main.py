import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    print(s[0].upper()+s[1:].lower())


if __name__ == '__main__':
    sys.exit(main())
