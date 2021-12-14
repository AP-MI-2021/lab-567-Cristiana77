from copy import deepcopy

def create_aeroport():
    return {
        "lista_curenta": [],
        "lista_undo": [[]],
        "lista_redo": []
    }

def get_lista_curenta(aeroport):
    return aeroport['lista_curenta']

def get_lista_undo(aeroport):
    return aeroport['lista_undo']

def get_lista_redo(aeroport):
    return aeroport['lista_redo']

def set_lista_curenta(aeroport, new_current_list):
    aeroport['lista_curenta'] = new_current_list

def adaugare_lista_undo(aeroport):
    lista_curenta = get_lista_curenta(aeroport)
    get_lista_undo(aeroport).append(deepcopy(lista_curenta))

def adaugare_lista_redo(aeroport):
    lista_curenta = get_lista_curenta(aeroport)
    get_lista_redo(aeroport).append(deepcopy(lista_curenta))

def clear_redo(aeroport):
    get_lista_redo(aeroport).clear()

def adaugare_undo_clear_redo(aeroport):
    adaugare_lista_undo(aeroport)
    clear_redo(aeroport)
