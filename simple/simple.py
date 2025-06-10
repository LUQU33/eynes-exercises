import random


def simple_list():
    dicts = []

    for i in range(10):
        diccionario = {"id": i+1, "age": random.randint(1, 99)}
        dicts.append(diccionario)
    
    return dicts

def sort_list(dicts):
    ordered_dicts = []

    for i in range(len(dicts)):
        pass