import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c = input().split()
    
    if a[-1]==b[0] and b[-1]==c[0]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    sys.exit(main())
