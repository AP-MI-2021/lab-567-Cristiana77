from Domain.rezervare import create_rezervare, get_clasa, get_pret
from Logic.operatiuni import sort_rezervari, compute_sum_prices_per_name, clasa_superioara, ieftinire, find_max1, find_max2, find_max3
from Logic.crud import find_rezervare

def test_ordonare():
    r1 = create_rezervare('id1', 'nume1', 'economy', 100, 'da')
    r2 = create_rezervare('id2', 'nume2', 'business', 200, 'nu')
    r3 = create_rezervare('id3', 'nume3', 'economy plus', 150, 'nu')

    sorted_list = sort_rezervari([r1,r2,r3])
    assert sorted_list[0] == r2
    assert sorted_list[1] == r3
    assert sorted_list[2] ==r1

def test_suma():
    r1 = create_rezervare('id1', 'nume1', 'economy', 100, 'da')
    r2 = create_rezervare('id2', 'nume2', 'business', 200, 'nu')
    r3 = create_rezervare('id3', 'nume3', 'economy plus', 150, 'nu')
    rezervari = [r1, r2, r3]
    suma_preturi_per_nume = compute_sum_prices_per_name(rezervari)
    assert suma_preturi_per_nume['nume1'] == 100
    assert suma_preturi_per_nume['nume2'] == 200

def test_clasa_superioara():
    r1 = create_rezervare('id1', 'nume1', 'economy', 100, 'da')
    r2 = create_rezervare('id2', 'nume2', 'economy plus', 150, 'nu')
    rezervari = [r1, r2]
    clasa_superioara(rezervari, 'nume1')
    assert get_clasa(find_rezervare(rezervari, 'id1')) == 'economy plus'
    clasa_superioara(rezervari, 'nume2')
    assert get_clasa(find_rezervare(rezervari, 'id2')) == 'business'

def test_ieftinire():
    r1 = create_rezervare('id1', 'nume1', 'economy', 100, 'da')
    r2 = create_rezervare('id2', 'nume2', 'economy plus', 200, 'nu')
    rezervari = [r1, r2]
    ieftinire(rezervari, 50)
    assert get_pret(find_rezervare(rezervari, 'id1')) == 50
    assert get_pret(find_rezervare(rezervari, 'id2')) ==200

def test_find_max1():
    r1 = create_rezervare('id1', 'nume1', 'economy', 100, 'da')
    r2 = create_rezervare('id2', 'nume2', 'economy plus', 200, 'nu')
    r3 = create_rezervare('id3', 'nume3', 'business', 150, 'nu')
    rezervari = [r1, r2, r3]
    assert find_max1(rezervari) == 100

def test_find_max2():
    r1 = create_rezervare('id1', 'nume1', 'economy', 100, 'da')
    r2 = create_rezervare('id2', 'nume2', 'economy plus', 200, 'nu')
    r3 = create_rezervare('id3', 'nume3', 'business', 150, 'nu')
    rezervari = [r1, r2, r3]
    assert find_max2(rezervari) == 200


def test_find_max3():
    r1 = create_rezervare('id1', 'nume1', 'economy', 100, 'da')
    r2 = create_rezervare('id2', 'nume2', 'economy plus', 200, 'nu')
    r3 = create_rezervare('id3', 'nume3', 'business', 150, 'nu')
    rezervari = [r1, r2, r3]
    assert find_max3(rezervari) == 150
    