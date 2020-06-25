import sympy as sym

def sieve(n):
    initlist = list(range(2, n+1))
    for x in range(2, n+1):
        for y in range(x, n+1, x):
            if x != y:
                try:
                    initlist.remove(y)
                except ValueError:
                    continue

    return initlist

def main():
    x = sieve(102)
    print(x, len(x))
    for y in x:
        print(sym.isprime(y))


if __name__ == '__main__':
    main()