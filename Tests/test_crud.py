from Logic.crud import add_rezervare, delete_rezervare, edit_rezervare, find_rezervare
from Domain.rezervare import create_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin_facut
from Domain.aeroport import create_aeroport, get_lista_curenta

def test_add_rezervari():
    aeroport = create_aeroport()

    rezervare_adaugata = create_rezervare(56, 'Sarah', 'economy', 1000, 'da')
    add_rezervare(aeroport, 56, 'Sarah', 'economy', 1000, 'da')
    assert len(get_lista_curenta(aeroport)) == 1
    assert get_id(rezervare_adaugata) == 56
    assert get_nume(rezervare_adaugata) == 'Sarah'
    assert get_clasa(rezervare_adaugata) == 'economy'
    assert get_pret(rezervare_adaugata) == 1000
    assert get_checkin_facut(rezervare_adaugata) == 'da'

    add_rezervare(aeroport, 123, 'John', 'business', 2000, 'nu')
    create_rezervare(123, 'John', 'business', 2000, 'nu')
    assert len(get_lista_curenta(aeroport)) == 2


def test_delete_rezervari():
    aeroport = create_aeroport()
    add_rezervare(aeroport, '44g', 'John', 'business', '2000', 'nu')
    add_rezervare(aeroport, '23r', 'Kevin', 'economy', '1000', 'da')
    assert len(get_lista_curenta(aeroport)) == 2
    delete_rezervare(aeroport, '2')
    assert len(get_lista_curenta(aeroport)) == 2

def test_edit_rezervari():
    aeroport = create_aeroport()

    add_rezervare(aeroport, '44g', 'Mara', 'business', '1500', 'da')
    add_rezervare(aeroport, '23r', 'Kevin', 'economy', '1000', 'da')
    assert len(get_lista_curenta(aeroport)) == 2
    edit_rezervare(aeroport, '23r', 'Ion', 'economy plus', '2300', 'nu')
    assert len(get_lista_curenta(aeroport)) == 2
    rezervare_modificata = find_rezervare(get_lista_curenta(aeroport), '23r')
    assert get_id(rezervare_modificata) == '23r'
    assert get_nume(rezervare_modificata) == 'Ion'
    assert get_clasa(rezervare_modificata) == 'economy plus'
    assert get_checkin_facut(rezervare_modificata) == 'nu'
