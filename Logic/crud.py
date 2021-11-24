from Domain.rezervare import create_rezervare, get_id, set_nume, set_clasa, set_pret, set_checkin_facut
from Logic.validare import validare_rezervare

def find_rezervare(rezervari, id):
    '''
    Find rezervare in rezervari with id
    If not found, we return None
    :param rezervari: lista
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
    :param rezervari: lista
    :param id: string
    :return:
    '''
    for i, rezervare in enumerate(rezervari):
        if get_id(rezervare) == id:
            return i
    return None

def add_rezervare(rezervari, id, nume, clasa, pret, checkin_facut):
    '''
    Adaugam in memorie, in lista de rezervari o rezervare formata din fieldurile: id, nume, clasa, pret, checkin_facut.
    :param rezervari: lista de rezervari
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: string
    :param checkin_facut: string
    :return:
    '''
    id, nume, clasa, pret, checkin_facut = validare_rezervare(id, nume, clasa, pret, checkin_facut)
    rezervare = create_rezervare(id, nume, clasa, pret, checkin_facut)
    return rezervari + [rezervare]

def delete_rezervare(rezervari, id):
    '''
    Stergem din memorie o rezervare cu ajutorul id-ului
    :param rezervari: lista de rezervari
    :param id: string
    :return:
    '''
    result_list = [rezervare for rezervare in rezervari if get_id(rezervare) != id]
    return result_list

def edit_rezervare(rezervari, id, nume, clasa, pret, checkin_facut):
    '''
    Modificarea in memorie a unei rezervari
    :param rezervari: lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :return:
    '''
    id, nume, clasa, pret, checkin_facut = validare_rezervare(id, nume, clasa, pret, checkin_facut)
    for rezervare in rezervari:
        if get_id(rezervare) == id:
            set_nume(rezervare, nume)
            set_clasa(rezervare, clasa)
            set_pret(rezervare, pret)
            set_checkin_facut(rezervare, checkin_facut)
