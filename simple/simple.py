import random


def simple_list():
    dicts = []

    for i in range(10):
        diccionario = {"id": i+1, "age": random.randint(1, 99)}
        dicts.append(diccionario)
    
    return dicts

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

print(sort_list(diccionarios))