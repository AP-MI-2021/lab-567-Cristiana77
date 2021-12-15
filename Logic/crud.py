from Domain.rezervare import create_rezervare, get_id, set_nume, set_clasa, set_pret, set_checkin_facut
from Logic.validare import validare_rezervare
from Domain.aeroport import *

def find_rezervare(rezervari, id):
    '''
    Find rezervare in rezervari with id
    If not found, we return None
    :param rezervari: dict
    :param id: string
    :return:
    '''
    for rezervare in rezervari:
        if get_id(rezervare) == id:
            return rezervare
    return None

def find_rezervare_index(rezervari, id):
    '''
    Find rezervari in rezervari with id
    If not found, we return None
    :param rezervari: dict
    :param id: string
    :return:
    '''
    for i, rezervare in enumerate(rezervari):
        if get_id(rezervare) == id:
            return i
    return None

def add_rezervare(aeroport, id, nume, clasa, pret, checkin_facut):
    '''
    Adaugam in memorie, in lista de rezervari o rezervare formata din fieldurile: id, nume, clasa, pret, checkin_facut.
    :param aeroport: dict
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: string
    :param checkin_facut: string
    :return:
    '''
    adaugare_undo_clear_redo(aeroport)
    rezervari = get_lista_curenta(aeroport)
    id, nume, clasa, pret, checkin_facut = validare_rezervare(id, nume, clasa, pret, checkin_facut)
    if find_rezervare_index(rezervari, id) != None:
        raise ValueError('Id duplicat.')
    rezervare = create_rezervare(id, nume, clasa, pret, checkin_facut)
    return set_lista_curenta(aeroport, rezervari + [rezervare])

def delete_rezervare(aeroport, id):
    '''
    Stergem din memorie o rezervare cu ajutorul id-ului
    :param aeroport: dict
    :param id: int
    :return:
    '''
    adaugare_undo_clear_redo(aeroport)
    rezervari = get_lista_curenta(aeroport)
    index = find_rezervare_index(rezervari, id)
    if index != None:
        rezervari.pop(index)

def edit_rezervare(aeroport, id, nume, clasa, pret, checkin_facut):
    '''
    Modificarea in memorie a unei rezervari
    :param aeroport: dict
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :return:
    '''
    adaugare_undo_clear_redo(aeroport)
    id, nume, clasa, pret, checkin_facut = validare_rezervare(id, nume, clasa, pret, checkin_facut)
    rezervari = get_lista_curenta(aeroport)
    for rezervare in rezervari:
        if get_id(rezervare) == id:
            set_nume(rezervare, nume)
            set_clasa(rezervare, clasa)
            set_pret(rezervare, pret)
            set_checkin_facut(rezervare, checkin_facut)
