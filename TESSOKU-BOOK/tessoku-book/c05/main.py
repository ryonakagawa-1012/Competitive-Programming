import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    ans = str(bin(2**10+(n-1)))

    print(ans.replace("0", "4").replace("1", "7")[3:])

if __name__ == '__main__':
    main()
