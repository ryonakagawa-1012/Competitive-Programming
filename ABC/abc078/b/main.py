import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    x, y, z = map(int, input().split())
    print((x-z) // (y+z))


if __name__ == '__main__':
    sys.exit(main())
