from Logic.crud import add_rezervare, delete_rezervare, edit_rezervare, find_rezervare
from Domain.rezervare import create_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin_facut

def test_add_rezervari():
    rezervari = []

    rezervare_adaugata = create_rezervare(56, 'Sarah', 'economy', 1000, 'da')
    rezervari = add_rezervare(rezervari, 56, 'Sarah', 'economy', 1000, 'da')
    assert len(rezervari) == 1
    assert get_id(rezervare_adaugata) == 56
    assert get_nume(rezervare_adaugata) == 'Sarah'
    assert get_clasa(rezervare_adaugata) == 'economy'
    assert get_pret(rezervare_adaugata) == 1000
    assert get_checkin_facut(rezervare_adaugata) == 'da'

    rezervari = add_rezervare(rezervari, 123, 'John', 'business', 2000, 'nu')
    create_rezervare(123, 'John', 'business', 2000, 'nu')
    assert len(rezervari) == 2


def test_delete_rezervari():
    r1 =create_rezervare('44g', 'John', 'business', '2000', 'nu')
    r2 = create_rezervare('23r', 'Kevin', 'economy', '1000', 'da')
    rezervari = [r1,r2]
    assert len(rezervari) == 2
    rezervari = delete_rezervare(rezervari, '44g')
    assert len(rezervari) == 1
    rezervari = delete_rezervare(rezervari, '299rgg')
    assert len(rezervari) == 1

def test_edit_rezervari():
    rezervari = []

    rezervari = add_rezervare(rezervari, '44g', 'Mara', 'business', '1500', 'da')
    rezervari = add_rezervare(rezervari, '23r', 'Kevin', 'economy', '1000', 'da')
    assert len(rezervari) == 2
    edit_rezervare(rezervari, '23r', 'Ion', 'economy plus', '2300', 'nu')
    assert len(rezervari) == 2
    rezervare_modificata = find_rezervare(rezervari, '23r')
    assert get_id(rezervare_modificata) == '23r'
    assert get_nume(rezervare_modificata) == 'Ion'
    assert get_clasa(rezervare_modificata) == 'economy plus'
    assert get_checkin_facut(rezervare_modificata) == 'nu'
