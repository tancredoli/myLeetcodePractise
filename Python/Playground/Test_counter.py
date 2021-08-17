from collections import Counter

if __name__ == '__main__':
    c1 = Counter('ANC')
    c2 = Counter('ABC')
    print(c2-c1)
    if c2-c1:
        print("yes")
    else:
        print('no')