from Domain.rezervare import create_rezervare
from Logic.operatiuni import sort_rezervari, compute_sum_prices_per_name

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
