import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    print(n)
    for i in range(1, n+1):
        ii = i+1 if i < n else 1
        print(i, ii)


if __name__ == '__main__':
    main()
