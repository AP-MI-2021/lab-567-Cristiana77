def validare_rezervare(id, nume, clasa, pret, checkin_facut):
    '''
    Validare params for a rezervare
    Throws a ValueError if fields are not correct
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: string
    :param checkin_facut: string
    :return:
    '''
    errors = []
    if id == '':
        errors.append('Id-ul nu poate fi vid')
    if nume == '':
        errors.append('Numele nu poate fi vid')
    if clasa != 'business' and clasa != 'economy' and clasa != 'economy plus':
        errors.append('Clasa nu poate fi vid, nici nu poate avea alte valori decat economy,economy plus sau business')
    try:
        pret = float(pret)
        if pret < 0:
            errors.append('Pretul trebuie sa fie pozitiv')
    except ValueError as ve:
        errors.append('Pretul trebuia sa fie numar real')
    if checkin_facut != 'da' and checkin_facut != 'nu':
        errors.append('Checkin-ul nu poate fi vid, nici nu poate contine alte valori decat da sau nu')
    if len(errors) != 0:
        raise ValueError(errors)

    return id, nume, clasa, pret, checkin_facut
