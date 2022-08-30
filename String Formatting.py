def print_formatted(number):
    tam = len(bin(number)[2:])
    for i in range(1, number+1):
        print(f'{str(i).rjust(tam)} {oct(i)[2:].rjust(tam)} {hex(i)[2:].upper().rjust(tam)} {bin(i)[2:].rjust(tam)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)