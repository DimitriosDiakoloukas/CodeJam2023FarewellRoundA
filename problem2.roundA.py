import sys

def read_input():
    return map(int, sys.stdin.readline().strip().split())

def read_list():
    return list(map(int, sys.stdin.readline().strip().split()))

def write_output(output):
    sys.stdout.write(str(output) + '\n')
    sys.stdout.flush()

def solve():
    m, r, n = read_input()
    x = read_list()
    last = 0
    ans1 = True
    ans2 = 0
    for i in range(n):
        if i+1 < n:
            if x[i+1]-r > last:
                if x[i]-r > last:
                    ans1 = False
                last = x[i]+r
                ans2 += 1
        else:
            if last < m:
                if x[i]-r > last:
                    ans1 = False
                last = x[i]+r
                ans2 += 1
    ans1 &= last >= m
    write_output(ans2 if ans1 else "IMPOSSIBLE")

def main():
    t = 1
    t, = read_input()
    for i in range(t):
        write_output("Case #" + str(i+1) + ": ")
        solve()

if __name__ == '__main__':
    main()
