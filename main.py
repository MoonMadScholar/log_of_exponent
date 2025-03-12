from math import log

def main():
    print(solve_for_ex(4,1024))

def solve_for_ex(a,b):
    """ex = 0
    for i in range(0,b):
        if b == a ** i:
            return i
    return ex
"""
    return round(log(b,a))
main()
