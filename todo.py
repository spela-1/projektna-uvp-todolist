import bottle
import model


SKRIVNOST = 'zeleni čaj z medom'

seznam = model.SeznamUporabnikov('uporabniki')


@bottle.get('/')
@bottle.get('/login')
def login():
    return bottle.template('views/login.tpl')


@bottle.post('/prijava')
def prijava():
    ime = bottle.request.forms.getunicode('ime')
    geslo = bottle.request.forms.getunicode('geslo')

    uporabnik = seznam.uporabniki.get(ime)
    if (uporabnik is not None) and (geslo == uporabnik.zasifrirano_geslo):
        bottle.response.set_cookie(
            'ime', '{}'.format(ime), secret=SKRIVNOST, path='/')
        return bottle.redirect('/projekti/tvoji')
    else:
        return bottle.redirect('/login')


@bottle.get('/sign-up')
def signup():
    return bottle.template('views/sign-up.tpl')


@bottle.post('/registracija')
def prijava():
    ime = bottle.request.forms.getunicode('ime')
    geslo = bottle.request.forms.getunicode('geslo')

    uporabnik = seznam.dodaj_uporabnika(ime, geslo)

    if uporabnik is not None:
        seznam.shrani_uporabnika(ime)
        bottle.response.set_cookie(
            'ime', '{}'.format(ime), secret=SKRIVNOST, path='/')
        return bottle.redirect('/projekti/tvoji')
    else:
        return bottle.redirect('/sign-up')


def projekti_za_danes(uporabnik):
    naloge = uporabnik.naloge_danes()
    return bottle.template('views/naloge_danes.tpl', naloge=naloge, ime_lastnika=uporabnik.ime)


@bottle.get('/projekti/<izbira>')
def pokazi_projekte(izbira):
    ime = bottle.request.get_cookie('ime', secret=SKRIVNOST)
    uporabnik = seznam.uporabniki[ime]

    if izbira == 'danes':
        return projekti_za_danes(uporabnik)

    projekti = []
    imena_uporabnikov = []
    if izbira == 'tvoji':
        projekti = uporabnik.seznam_projektov
        imena_uporabnikov = [ime for p in projekti]
    elif izbira == 'deljeni':
        projekti, imena_uporabnikov = seznam.deljeni_projekti(ime)

    return bottle.template('views/projekti.tpl', projekti=projekti, imena_uporabnikov=imena_uporabnikov, izbira=izbira)


@bottle.get('/projekt/<ime_lastnika>/<id_projekta:int>')
def pokazi_projekte(ime_lastnika, id_projekta):
    ime = bottle.request.get_cookie('ime', secret=SKRIVNOST)
    uporabnik = seznam.uporabniki[ime_lastnika]

    projekt = None
    for pr in uporabnik.seznam_projektov:
        if pr.id == id_projekta:
            if ime == ime_lastnika or ime in pr.deljeno_z:
                projekt = pr
            break

    if projekt is not None:
        return bottle.template('views/projekt.tpl', projekt=projekt, ime_lastnika=ime_lastnika)
    else:
        return bottle.redirect('/projekti/tvoji')


@bottle.get('/opravi-nalogo/<ime_lastnika>/<id_projekta:int>/<id_naloge:int>')
def opravi_nalogo(ime_lastnika, id_projekta, id_naloge):
    ime = bottle.request.get_cookie('ime', secret=SKRIVNOST)
    uporabnik = seznam.uporabniki[ime_lastnika]

    naloga = None
    for pr in uporabnik.seznam_projektov:
        if pr.id == id_projekta:
            for na in pr.seznam_nalog:
                if na.id == id_naloge:
                    if ime == ime_lastnika or ime in pr.deljeno_z:
                        naloga = na
                    break

    if naloga is not None:
        naloga.opravljeno = not naloga.opravljeno
        seznam.shrani_uporabnika(ime_lastnika)
    bottle.redirect('/projekt/{}/{}'.format(ime_lastnika, id_projekta))


@bottle.post('/nov-projekt')
def nov_projekt():
    ime = bottle.request.get_cookie('ime', secret=SKRIVNOST)
    uporabnik = seznam.uporabniki[ime]

    ime_projekta = bottle.request.forms.getunicode('ime')
    uporabnik.nov_projekt(ime_projekta)

    seznam.shrani_uporabnika(ime)
    bottle.redirect('/projekti/tvoji')


@bottle.post('/nova-naloga/<ime_lastnika>/<id_projekta:int>')
def nova_naloga(ime_lastnika, id_projekta):
    ime = bottle.request.get_cookie('ime', secret=SKRIVNOST)
    uporabnik = seznam.uporabniki[ime_lastnika]

    projekt = None
    for pr in uporabnik.seznam_projektov:
        if pr.id == id_projekta:
            if ime == ime_lastnika or ime in pr.deljeno_z:
                projekt = pr
            break

    if projekt is not None:
        tekst = bottle.request.forms.getunicode('tekst')
        prioriteta = int(bottle.request.forms.getunicode('prioriteta'))
        datum = bottle.request.forms.getunicode('datum')
        ura = bottle.request.forms.getunicode('ura')

        if len(datum) > 0:
            datum = [int(i) for i in datum.split('-')]
        else:
            datum = []

        if len(ura) > 0:
            ura = [int(i) for i in ura.split(':')]
        else:
            ura = []

        print(datum, ura)

        projekt.nova_naloga(tekst, datum, ura, prioriteta)
        seznam.shrani_uporabnika(ime_lastnika)
        bottle.redirect('/projekt/{}/{}'.format(ime_lastnika, id_projekta))
    else:
        bottle.redirect('/projekti/tvoji')


@bottle.post('/deli/<ime_lastnika>/<id_projekta:int>')
def deli_z(ime_lastnika, id_projekta):
    ime = bottle.request.get_cookie('ime', secret=SKRIVNOST)
    uporabnik = seznam.uporabniki[ime_lastnika]

    ime_osebe = bottle.request.forms.getunicode('oseba')

    projekt = None
    for pr in uporabnik.seznam_projektov:
        if pr.id == id_projekta:
            if ime == ime_lastnika or ime in pr.deljeno_z:
                projekt = pr
            break

    if projekt is not None:
        seznam.deli_projekt(ime_lastnika, projekt.id, ime_osebe)
        seznam.shrani_uporabnika(ime_lastnika)
        seznam.shrani_uporabnika(ime_osebe)
        bottle.redirect('/projekt/{}/{}'.format(ime_lastnika, id_projekta))
    else:
        bottle.redirect('/projekti/tvoji')


@bottle.get('/izbrisi-projekt/<id_projekta:int>')
def deli_z(id_projekta):
    ime = bottle.request.get_cookie('ime', secret=SKRIVNOST)
    uporabnik = seznam.uporabniki[ime]

    projekt = None
    for pr in uporabnik.seznam_projektov:
        if pr.id == id_projekta:
            projekt = pr
            break

    if projekt is not None:
        uporabnik.izbrisi_projekt(projekt.ime)
        seznam.shrani_uporabnika(ime)

    bottle.redirect('/projekti/tvoji')


@bottle.get('/odjava')
def odjava():
    bottle.response.set_cookie(
        'ime', '', secret=SKRIVNOST, path='/')
    bottle.redirect('/login')


bottle.run()
