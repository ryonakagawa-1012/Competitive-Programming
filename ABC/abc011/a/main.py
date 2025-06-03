import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print(n%12+1)

if __name__ == '__main__':
    sys.exit(main())
