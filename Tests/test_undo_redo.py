from Logic.undo_redo import *
from Logic.crud import add_rezervare
from Domain.aeroport import create_aeroport, get_lista_curenta

def test_undo_redo():
    aeroport = create_aeroport()

    add_rezervare(aeroport, 'id1', 'nume1', 'economy', 100, 'da')
    add_rezervare(aeroport, 'id2', 'nume2', 'business', 200, 'nu')
    add_rezervare(aeroport, 'id3', 'nume3', 'economy plus', 150, 'nu')
    assert len(get_lista_curenta(aeroport)) == 3

    apply_undo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 2

    apply_undo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 1

    apply_undo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 0

    apply_redo(aeroport)
    apply_redo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 2

    apply_redo(aeroport)
    apply_undo(aeroport)
    apply_redo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 3
