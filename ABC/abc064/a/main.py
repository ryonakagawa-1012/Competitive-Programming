import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    r, g, b = input().split()

    if int(r+g+b) % 4 == 0:
        print("YES")
    else:
        print("NO")
        


if __name__ == '__main__':
    sys.exit(main())
