if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 or 5 < n < 21:
        print ("Weird")
    else:
        print ("Not Weird")