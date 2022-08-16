if __name__ == '__main__':
    num = int(input())
    list = map(int, input().split())
    tup = tuple(list)
    print(hash(tup))