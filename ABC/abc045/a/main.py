import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a = int(input())
    b = int(input())
    h = int(input())
    print(((a+b)*h)//2)


if __name__ == '__main__':
    sys.exit(main())
