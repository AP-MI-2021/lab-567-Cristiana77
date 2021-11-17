from Logic.crud import add_rezervare, delete_rezervare, edit_rezervare, find_rezervare
from Domain.rezervare import create_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin_facut

def test_add_rezervari():
    rezervari = []

    rezervare_adaugata = create_rezervare('56b', 'Sarah', 'economy', '1000', 'da')
    add_rezervare(rezervari, '56b', 'Sarah', 'economy', '1000', 'da')
    assert len(rezervari) == 1
    assert rezervari[0] == rezervare_adaugata
    assert get_id(rezervari[0]) == '56b'
    assert get_nume(rezervari[0]) == 'Sarah'
    assert get_clasa(rezervari[0]) == 'economy'
    assert get_pret(rezervari[0]) == '1000'
    assert get_checkin_facut(rezervari[0]) == 'da'

    add_rezervare(rezervari, '123', 'John', 'business', '2000', 'nu')
    rezervare_adaugata_2 = create_rezervare('123', 'John', 'business', '2000', 'nu')
    assert len(rezervari) == 2
    assert rezervari[0] == rezervare_adaugata
    assert rezervari[1] == rezervare_adaugata_2

def test_delete_rezervari():
    rezervari = []

    add_rezervare(rezervari, '44g', 'Mara', 'business', '1500', 'da')
    add_rezervare(rezervari, '23r', 'Kevin', 'economy', '1000', 'da')
    assert len(rezervari) == 2
    delete_rezervare(rezervari, '44g')
    assert len(rezervari) == 1
    delete_rezervare(rezervari, '23r')
    assert len(rezervari) == 1

def test_edit_rezervari():
    rezervari = []

    add_rezervare(rezervari, '44g', 'Mara', 'business', '1500', 'da')
    add_rezervare(rezervari, '23r', 'Kevin', 'economy', '1000', 'da')
    assert len(rezervari) == 2
    edit_rezervare(rezervari, '23r', 'Ion', 'economy plus', '2300', 'nu')
    assert len(rezervari) == 2
    rezervare_modificata = find_rezervare(rezervari, '23r')
    assert get_id(rezervare_modificata) == '23r'
    assert get_nume(rezervare_modificata) == 'Ion'
    assert get_clasa(rezervare_modificata) == 'economy plus'
    assert get_pret(rezervare_modificata) == '2300'
    assert get_checkin_facut(rezervare_modificata) == 'nu'
