from Tests.test_crud import test_add_rezervari, test_delete_rezervari, test_edit_rezervari
from Tests.domain_test import rezervare_test
from Tests.operatiuni_test import test_ordonare, test_suma, test_clasa_superioara, test_ieftinire, test_find_max1, test_find_max2, test_find_max3
from Tests.test_undo_redo import test_undo_redo

def run_all_tests():
    test_add_rezervari()
    test_delete_rezervari()
    test_edit_rezervari()
    rezervare_test()
    test_ordonare()
    test_suma()
    test_clasa_superioara()
    test_ieftinire()
    test_find_max1()
    test_find_max2()
    test_find_max3()
    test_undo_redo()
