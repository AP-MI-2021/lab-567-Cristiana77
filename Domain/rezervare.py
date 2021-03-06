def create_rezervare(id, nume, clasa, pret, checkin_facut):
    '''
    Crearea unui dictionar care reprezinta o rezervare
    :param id: string
    :param nume: string
    :param clasa: string: 'economy','economy plus',or 'business'
    :param pret: float
    :param checkin_facut: string: 'da' sau 'nu'
    :return: dict
    '''
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin_facut": checkin_facut
    }

def get_id(rezervare):
    '''
    Id-ul rezervarii
    :param rezervare: dict
    :return: id - string
    '''
    return rezervare['id']

def set_id(rezervare, id):
    '''
    Noul id
    :param rezervare: dict
    :param id: string
    :return:
    '''
    rezervare['id'] = id

def get_nume(rezervare):
    '''
    Numele pe care este facuta rezervarea
    :param rezervare: dict
    :return: nume - string
    '''
    return rezervare['nume']

def set_nume(rezervare, nume):
    '''
    Noul nume
    :param rezervare: dict
    :param nume: string
    :return:
    '''
    rezervare['nume'] = nume

def get_clasa(rezervare):
    '''
    Clasa la care este facuta rezervarea
    :param rezervare: dict
    :return: clasa - string
    '''
    return rezervare['clasa']

def set_clasa(rezervare, clasa):
    '''
    Noua clasa
    :param rezervare: dict
    :param clasa: string
    :return:
    '''
    rezervare['clasa'] = clasa

def get_pret(rezervare):
    '''
    Pretul calatoriei
    :param rezervare: dict
    :return: pret - float
    '''
    return rezervare['pret']

def set_pret(rezervare, pret):
    '''
    Noul pret
    :param rezervare: dict
    :param pret: float
    :return:
    '''
    rezervare['pret'] = pret

def get_checkin_facut(rezervare):
    '''
    Status checkin
    :param rezervare: dict
    :return: checkin_facut - string
    '''
    return rezervare['checkin_facut']

def set_checkin_facut(rezervare, checkin_facut):
    '''
    Noul checkin_facut
    :param rezervare: dict
    :param checkin_facut: string
    :return:
    '''
    rezervare['checkin_facut'] = checkin_facut

def to_str(rezervare):
    return f'ID={get_id(rezervare)}, nume={get_nume(rezervare)}, clasa={get_clasa(rezervare)}, pret={get_pret(rezervare)}, checkin_facut={get_checkin_facut(rezervare)}'
