from Domain.rezervare import *

def sort_rezervari(rezervari):
    '''
    Ordonare descrescatoare dupa pret
    :param rezervari: lista
    :return:
    '''
    return sorted(rezervari, key=sorting_criteria, reverse=True)

def sorting_criteria(rezervare):
    '''
    Criteriul de sortare
    :param rezervare: lista
    :return:
    '''
    return get_pret(rezervare)

def compute_sum_prices_per_name(rezervari):
    '''
    Afișarea sumelor prețurilor pentru fiecare nume.
    :param rezervari: lista
    :return:
    '''
    result = {}
    for rezervare in rezervari:
        nume = get_nume(rezervare)
        pret = get_pret(rezervare)
        if nume in result:
            result[nume] += pret
        else:
            result[nume] = pret
    return result
