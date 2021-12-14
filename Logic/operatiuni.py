from Domain.rezervare import get_pret, get_nume, get_clasa, get_checkin_facut, set_pret, set_clasa
from Domain.aeroport import get_lista_curenta, adaugare_undo_clear_redo

def sort_rezervari(aeroport):
    '''
    Ordonare descrescatoare dupa pret
    :param aeroport: dict
    :return:
    '''
    rezervari = get_lista_curenta(aeroport)
    return sorted(rezervari, key=lambda rezervare: get_pret(rezervare), reverse=True)

def compute_sum_prices_per_name(aeroport):
    '''
    Afișarea sumelor prețurilor pentru fiecare nume.
    :param aeroport: dict
    :return:
    '''
    result = {}
    rezervari = get_lista_curenta(aeroport)
    for rezervare in rezervari:
        nume = get_nume(rezervare)
        pret = get_pret(rezervare)
        if nume in result:
            result[nume] += pret
        else:
            result[nume] = pret
    return result

def clasa_superioara(aeroport, nume):
    '''
    Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
    :param aeroport: dict
    :return:
    '''
    adaugare_undo_clear_redo(aeroport)
    rezervari = get_lista_curenta(aeroport)
    for rezervare in rezervari:
        if nume == get_nume(rezervare):
            if get_clasa(rezervare) == 'economy':
                set_clasa(rezervare, 'economy plus')
            elif get_clasa(rezervare) == 'economy plus':
                set_clasa(rezervare, 'business')

def ieftinire(aeroport, procentaj):
    '''
    Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.
    :param aeroport: dict
    :param procentaj: float
    :return:
    '''
    adaugare_undo_clear_redo(aeroport)
    rezervari = get_lista_curenta(aeroport)
    for rezervare in rezervari:
        if get_checkin_facut(rezervare) == 'da':
            pret_redus = float(get_pret(rezervare)) - ((float(get_pret(rezervare)) * procentaj) // 100)
            set_pret(rezervare, pret_redus)

def find_max1(aeroport):
    '''
    Pretul maxim din clasa economy.
    :param aeroport: dict
    :return:
    '''
    rezervari = get_lista_curenta(aeroport)
    max1 = 0
    for rezervare in rezervari:
        if get_clasa(rezervare) == 'economy' and get_pret(rezervare) > max1:
            max1 = get_pret(rezervare)
    return max1

def find_max2(aeroport):
    '''
    Pretul maxim din clasa economy plus.
    :param aeroport: dict
    :return:
    '''
    rezervari = get_lista_curenta(aeroport)
    max2 = 0
    for rezervare in rezervari:
        if get_clasa(rezervare) == 'economy plus' and get_pret(rezervare) > max2:
            max2 = get_pret(rezervare)
    return max2

def find_max3(aeroport):
    '''
    Pretul maxim din clasa business.
    :param aeroport: dict
    :return:
    '''
    rezervari = get_lista_curenta(aeroport)
    max3 = 0
    for rezervare in rezervari:
        if get_clasa(rezervare) == 'business' and get_pret(rezervare) > max3:
            max3 = get_pret(rezervare)
    return max3
