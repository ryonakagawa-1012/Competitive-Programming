import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    if n % 2 == 0:
        print("Blue")
    else:
        print("Red")


if __name__ == '__main__':
    sys.exit(main())
