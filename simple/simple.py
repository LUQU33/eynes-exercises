import random

# Funcion que genera los 10 diccionarios


def simple_list():
    dicts = []

    for i in range(10):
        diccionario = {"id": i+1, "age": random.randint(1, 100)}
        dicts.append(diccionario)

    return dicts

# Funcion que ordena los diccionarios por edad en orden ascendente


def sort_list(dicts):
    for i in range(1, len(dicts)):
        actual = dicts[i]
        j = i - 1

        while j >= 0 and dicts[j]["age"] > actual["age"]:
            dicts[j + 1] = dicts[j]
            j -= 1

        dicts[j + 1] = actual

    return dicts


diccionarios = simple_list()
diccionarios_ord = sort_list(diccionarios)

# For para muestra por pantalla de los diccionarios ordenados
for i in range(len(diccionarios)):
    print(f"DICCIONARIO[{i}]: {diccionarios_ord[i]}")
