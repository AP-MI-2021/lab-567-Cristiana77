import sys

from Domain.rezervare import to_str
from Logic.crud import add_rezervare, delete_rezervare, edit_rezervare
from Logic.operatiuni import sort_rezervari, compute_sum_prices_per_name, clasa_superioara, ieftinire, find_max1, find_max2, find_max3
from Logic.validare import validare_procent
from Domain.aeroport import *
from Logic.undo_redo import apply_redo, apply_undo

def print_meniu_undo_redo():
    print('''
    MENIU -Undo/ Redo
    1. Undo 
    2. Redo
    3. Inapoi
    ''')

def print_meniu():
    print('''
    MENIU
    1. CRUD
    2. Operatiuni
    3. Undo/Redo
    4. Iesire    
    ''')

def print_crud_meniu():
    print('''
    MENIU Crud
    1. Adaugare
    2. Stergere
    3. Modificare
    4. Afisare toate rezervarile
    5. Inapoi 
    ''')

def print_operatiuni_meniu():
    print('''
    MENIU Operatiuni
    1. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
    2. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.
    3. Determinarea prețului maxim pentru fiecare clasă.
    4. Ordonarea rezervărilor descrescător după preț.
    5. Afișarea sumelor prețurilor pentru fiecare nume.
    6. Inapoi
    ''')

def run_crud_ui(aeroport):
    '''

    :param aeroport: dict
    :return:
    '''

    def handle_show_all(aeroport):
        '''
        Afisare lista de rezervari din memorie
        :param aeroport: dict
        :return:
        '''
        rezervari = get_lista_curenta(aeroport)
        for rezervare in rezervari:
            print(to_str(rezervare))


    def handle_add_rezervare_ui(aeroport):
        '''
        Adaugam o rezervare
        :param aeroport: dict
        :return:
        '''
        id = input('Dati id-ul rezervarii: ')
        nume = input('Dati numele: ')
        clasa = input('Precizati tipul clasei: ')
        pret = input('Dati pretul: ')
        checkin_facut = input('Precizati daca a facut checkin: ')
        try:
            add_rezervare(aeroport, id, nume, clasa, pret, checkin_facut)
            print('Rezervarea a fost adaugata cu succes.')
            return aeroport
        except ValueError as ve:
            print('Au aparut erori: ', ve)
        except:
            print('Unknown error.')
        return aeroport

    def handle_delete_rezervare_ui(aeroport):
        '''
        Sterge o rezervare
        :param aeroport: dict
        :return:
        '''
        id = input('Dati id-ul rezervarii: ')
        try:
            delete_rezervare(aeroport, id)
            print('Rezervarea a fost stearsa cu succes.')
            return aeroport
        except ValueError as ve:
            print('Au aparut erori: ', ve)
        except:
            print('Unknown error.')
        return aeroport

    def handle_edit_rezervare_ui(aeroport):
        '''
        Modificam o rezervare
        :param aeroport: dict
        :return:
        '''
        id = input('Dati id-ul rezervarii: ')
        nume = input('Dati numele: ')
        clasa = input('Precizati tipul clasei: ')
        pret = float(input('Dati pretul: '))
        checkin_facut = input('Precizati daca a facut checkin: ')
        try:
            edit_rezervare(aeroport, id, nume, clasa, pret, checkin_facut)
            print('Rezervarea a fost modificata cu succes.')
            return aeroport
        except ValueError as ve:
            print('Au aparut erori: ', ve)
        except:
            print('Unknown error.')
        return aeroport

    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            aeroport = handle_add_rezervare_ui(aeroport)
        elif cmd == '2':
            aeroport = handle_delete_rezervare_ui(aeroport)
        elif cmd == '3':
            aeroport = handle_edit_rezervare_ui(aeroport)
        elif cmd == '4':
            handle_show_all(aeroport)
        elif cmd == '5':
            run_console(aeroport)
        else:
            print('Comanda invalida')

def run_operatiuni_ui(aeroport):
    '''
    Operatiuni pe lista
    :param aeroport: dict
    :return:
    '''

    def handle_mutare(aeroport):
        '''
        Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
        :param aeroport: dict
        :return:
        '''
        nume = input('Dati numele a carui clasa vreti sa fie trecuta la una superioara: ')
        aeroport = clasa_superioara(aeroport, nume)
        print('Rezervarile au fost mutate la o clasa superioara cu succes.')
        return aeroport

    def handle_ieftinire(aeroport):
        '''
        Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.
        :param aeroport: dict
        :return:
        '''
        procentaj = input('Procentajul de ieftinire: ')
        try:
            procentaj = validare_procent(procentaj)
            ieftinire(aeroport, procentaj)
            print('Ieftinirea a fost facuta cu succes.')
            print(aeroport)
            return aeroport
        except ValueError as ve:
            print(ve)

    def handle_maxim(aeroport):
        '''
        Determinarea prețului maxim pentru fiecare clasă.
        :param aeroport: dict
        :return:
        '''
        max1 = find_max1(aeroport)
        max2 = find_max2(aeroport)
        max3 = find_max3(aeroport)
        print('Pretul maxim clasei economy este: ', max1)
        print('Pretul maxim clasei economy plus este: ', max2)
        print('Pretul maxim clasei business este: ', max3)

    def handle_ordonare(aeroport):
        '''
        Ordonarea rezervărilor descrescător după preț.
        :param aeroport: dict
        :return:
        '''
        sort_rezervari(aeroport)
        print('Rezervarile au fost ordonate cu succes.')
        return aeroport

    def handle_suma(aeroport):
        '''
        Afișarea sumelor prețurilor pentru fiecare nume.
        :param aeroport: dict
        :return:
        '''
        print(compute_sum_prices_per_name(aeroport))

    while True:
        print_operatiuni_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            aeroport = handle_mutare(aeroport)
        elif cmd == '2':
            aeroport = handle_ieftinire(aeroport)
        elif cmd == '3':
            aeroport = handle_maxim(aeroport)
        elif cmd == '4':
            aeroport = handle_ordonare(aeroport)
        elif cmd == '5':
            aeroport = handle_suma(aeroport)
        elif cmd == '6':
            run_console(aeroport)
        else:
            print('Comanda invalida')

def run_undo_redo_ui(aeroport):
    '''

    :param aeroport: dict
    :return:
    '''

    def handle_undo(aeroport):
        apply_undo(aeroport)
        print('Undo facut cu succes.')

    def handle_redo(aeroport):
        apply_redo(aeroport)
        print('Redo facut cu succes.')

    while True:
        print_meniu_undo_redo()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_undo(aeroport)
        elif cmd == '2':
            handle_redo(aeroport)
        elif cmd == '3':
            run_console(aeroport)
        else:
            print('Comanda invalida')

def run_console(aeroport):
    '''

    :param aeroport: dict
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(aeroport)
        elif cmd == '2':
            run_operatiuni_ui(aeroport)
        elif cmd == '3':
            run_undo_redo_ui(aeroport)
        elif cmd == '4':
            print('La revedere!')
            sys.exit(0)
        else:
            print('Comanda invalida')
