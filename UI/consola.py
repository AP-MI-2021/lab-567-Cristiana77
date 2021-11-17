from Domain.rezervare import to_str
from Logic.crud import add_rezervare, delete_rezervare, edit_rezervare

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

def run_crud_ui(rezervari):
    '''

    :param rezervari: Lista de rezervari
    :return:
    '''

    def handle_show_all(rezervari):
        '''
        Afisare lista de rezervari din memorie
        :param rezervari: Lista de rezervari
        :return:
        '''
        for rezervare in rezervari:
            print(to_str(rezervare))


    def handle_add_rezervare_ui(rezervari):
        '''
        Adaugam o rezervare
        :param rezervari: lista de rezervari
        :return:
        '''
        id = input('Dati id-ul rezervarii: ')
        nume = input('Dati numele: ')
        clasa = input('Precizati tipul clasei: ')
        pret = float(input('Dati pretul: '))
        checkin_facut = input('Precizati daca a facut checkin: ')
        add_rezervare(rezervari, id, nume, clasa, pret, checkin_facut)
        print('Rezervarea a fost adaugata cu succes.')

    def handle_delete_rezervare_ui(rezervari):
        '''
        Sterge o rezervare
        :param rezervari: lista de rezervari
        :return:
        '''
        id = input('Dati id-ul rezervarii: ')
        delete_rezervare(rezervari, id)
        print('Rezervarea a fost stearsa cu succes.')

    def handle_edit_rezervare_ui(rezervari):
        '''
        Modificam o rezervare
        :param rezervari: lista
        :return:
        '''
        id = input('Dati id-ul rezervarii: ')
        nume = input('Dati numele: ')
        clasa = input('Precizati tipul clasei: ')
        pret = float(input('Dati pretul: '))
        checkin_facut = input('Precizati daca a facut checkin: ')
        edit_rezervare(rezervari, id, nume, clasa, pret, checkin_facut)
        print('Rezervarea a fost modificata cu succes.')

    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_add_rezervare_ui(rezervari)
        elif cmd == '2':
            handle_delete_rezervare_ui(rezervari)
        elif cmd == '3':
            handle_edit_rezervare_ui(rezervari)
        elif cmd == '4':
            handle_show_all(rezervari)
        elif cmd == '5':
            break
        else:
            print('Comanda invalida')

def run_operatiuni_ui(rezervari):
    '''
    Operatiuni pe lista
    :param rezervari: lista de rezervari
    :return:
    '''

    def handle_mutare(rezervari):
        '''
        Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
        :param rezervari: lista de rezervari
        :return:
        '''
    pass

    while True:
        print_operatiuni_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_mutare(rezervari)
        elif cmd == '2':
            pass
        elif cmd == '3':
            pass
        elif cmd == '4':
            pass
        elif cmd == '5':
            pass
        elif cmd == '6':
            break
        else:
            print('Comanda invalida')

def run_undo_redo_ui(rezervari):
    pass

def run_console(rezervari):
    '''

    :param rezervari: lista de rezervari
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(rezervari)
        elif cmd == '2':
            run_operatiuni_ui(rezervari)
        elif cmd == '3':
            run_undo_redo_ui(rezervari)
        elif cmd == '4':
            break
        else:
            print('Comanda invalida')
