from Domain.rezervare import create_rezervare, get_clasa, get_pret
from Logic.operatiuni import sort_rezervari, compute_sum_prices_per_name, clasa_superioara, ieftinire, find_max1, find_max2, find_max3
from Logic.crud import find_rezervare, add_rezervare
from Domain.aeroport import create_aeroport, get_lista_curenta

def test_ordonare():
    aeroport = create_aeroport()
    add_rezervare(aeroport, 'id1', 'nume1', 'economy', 100, 'da')
    add_rezervare(aeroport, 'id2', 'nume2', 'business', 200, 'nu')
    add_rezervare(aeroport, 'id3', 'nume3', 'economy plus', 150, 'nu')
    assert sort_rezervari(aeroport) == [{'id': 'id2', 'nume': 'nume2', 'clasa': 'business', 'pret': 200, 'checkin_facut': 'nu'}, {'id': 'id3', 'nume': 'nume3', 'clasa': 'economy plus', 'pret': 150, 'checkin_facut': 'nu'},  {'id': 'id1', 'nume': 'nume1', 'clasa': 'economy', 'pret': 100, 'checkin_facut': 'da'}]


def test_suma():
    aeroport = create_aeroport()
    add_rezervare(aeroport, 'id1', 'nume1', 'economy', 100, 'da')
    add_rezervare(aeroport, 'id2', 'nume2', 'business', 200, 'nu')
    add_rezervare(aeroport, 'id3', 'nume3', 'economy plus', 150, 'nu')

    suma_preturi_per_nume = compute_sum_prices_per_name(aeroport)
    assert suma_preturi_per_nume['nume1'] == 100
    assert suma_preturi_per_nume['nume2'] == 200

def test_clasa_superioara():
    aeroport = create_aeroport()
    add_rezervare(aeroport, 'id1', 'nume1', 'economy', 100, 'da')
    add_rezervare(aeroport, 'id2', 'nume2', 'economy plus', 150, 'nu')

    clasa_superioara(aeroport, 'nume1')
    assert get_clasa(find_rezervare(get_lista_curenta(aeroport), 'id1')) == 'economy plus'
    clasa_superioara(aeroport, 'nume2')
    assert get_clasa(find_rezervare(get_lista_curenta(aeroport), 'id2')) == 'business'

def test_ieftinire():
    aeroport = create_aeroport()
    add_rezervare(aeroport, 'id1', 'nume1', 'economy', 100, 'da')
    add_rezervare(aeroport, 'id2', 'nume2', 'economy plus', 200, 'nu')
    ieftinire(aeroport, 50)
    assert get_pret(find_rezervare(get_lista_curenta(aeroport), 'id1')) == 50
    assert get_pret(find_rezervare(get_lista_curenta(aeroport), 'id2')) ==200

def test_find_max1():
    aeroport = create_aeroport()
    add_rezervare(aeroport, 'id1', 'nume1', 'economy', 100, 'da')
    add_rezervare(aeroport, 'id2', 'nume2', 'economy plus', 200, 'nu')
    add_rezervare(aeroport, 'id3', 'nume3', 'business', 150, 'nu')
    assert find_max1(aeroport) == 100

def test_find_max2():
    aeroport =create_aeroport()
    add_rezervare(aeroport, 'id1', 'nume1', 'economy', 100, 'da')
    add_rezervare(aeroport, 'id2', 'nume2', 'economy plus', 200, 'nu')
    add_rezervare(aeroport, 'id3', 'nume3', 'business', 150, 'nu')
    assert find_max2(aeroport) == 200


def test_find_max3():
    aeroport = create_aeroport()
    add_rezervare(aeroport, 'id1', 'nume1', 'economy', 100, 'da')
    add_rezervare(aeroport, 'id2', 'nume2', 'economy plus', 200, 'nu')
    add_rezervare(aeroport,'id3', 'nume3', 'business', 150, 'nu')
    assert find_max3(aeroport) == 150
    