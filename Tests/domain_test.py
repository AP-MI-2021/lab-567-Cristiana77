from Domain.rezervare import *

def rezervare_test():
    rezervare = create_rezervare('67b', 'Popescu', 'economy', '1000', 'da')
    assert get_id(rezervare) == '67b'
    assert get_nume(rezervare) == 'Popescu'
    assert get_clasa(rezervare) == 'economy'
    assert get_pret(rezervare) == '1000'
    assert get_checkin_facut(rezervare) == 'da'

    set_nume(rezervare, 'Popa')
    assert get_nume(rezervare) == 'Popa'
    set_pret(rezervare, '1200')
    assert get_pret(rezervare) == '1200'
    set_clasa(rezervare, 'business')
    assert get_clasa(rezervare) == 'business'
    set_checkin_facut(rezervare, 'nu')
    assert get_checkin_facut(rezervare) == 'nu'
