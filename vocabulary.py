def add_prefix_un(palabra):
    """Le añadimos 'un' al principio de la palabra

    :param palabra: str
    :return: str - palabra con 'un' al inicio.
    """

    return ('un' + palabra)
# print(add_prefix_un('happy'))


def make_word_groups(lista_palabras: list) -> str:
    """Le añadimos prefijo a una lista de palabras.

    :param lista_palabra: list
    :return: str - palabras con el prefijo aplicado

    Tomamos una lista de palabras y regresamos un string con el prefijo 
    aplicado a las palabras, separadas por '::'

    Ejemplo: lista('en', 'close', 'joy', 'lighten'),
    retornamos el sig. string: 'en :: enclose :: enjoy :: enlighten'.
    """
    new_list = []
    for palabra in lista_palabras[1:]:
        new_list.append(lista_palabras[0]+palabra)
    y = lista_palabras[0] + ' :: ' + ' :: '.join(new_list)
    return y
#palabras = ['pre', 'serve', 'dispose', 'position']
# print(make_word_groups(palabras))


def remove_suffix_ness(word):
    """Removemos el sufijo.

    :param word: str.
    :return: str - palabra sin sufijo y con gramaticamente correcto.

    Ejemplo: "heaviness" -> "heavy", pero "sadness" -> "sad".
    """
    new_word = word[: -4]
    if new_word[-1] == 'i':
        lista = list(new_word)
        lista[-1] = 'y'
        print(lista)
        x = "".join(lista)
        print(x)
        return lista
    return new_word
# print(remove_suffix_ness('crabbiness'))


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    :param sentence: str
    :param index: int - index de la palabra que hay que cambiar.
    :return: str - palabra cambiada a verbo

    Ejemplo, ("It got dark as the sun set", 2) becomes "darken".
    """
    lista = sentence.split()
    verbo = lista[index]
    if verbo[-1] == '.':
        return (verbo[:-1] + 'en')
    return (verbo + "en")


print(adjective_to_verb("It got dark as the sun set", 2))
