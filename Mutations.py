def mutate_string(string, position, character):
    lista = list(string)
    lista[position] = character
    remover = ["'", "[", "]", ",", " "]
    lista_replace = repr(lista)
    for rmv in remover:
        lista_replace = lista_replace.replace(rmv, '')
    return lista_replace

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)