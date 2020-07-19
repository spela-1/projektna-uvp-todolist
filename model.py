class Naloga():
    def __init__(self, id, tekst, datum=None , ura=None, prioriteta=None):
        self.tekst = tekst
        self.datum = datum
        self.ura = ura
        self.opravljeno = False
        self.prioriteta = prioriteta
        self.id = id


class Projekt():
    def __init__(self, ime):
        self.ime = ime
        self.seznam_nalog = []
        self.naslednji_id = 0
    
    def nova_naloga(self, tekst, datum=None , ura=None, prioriteta=None):
        naloga = Naloga(self.naslednji_id, tekst, datum, ura, prioriteta)
        self.seznam_nalog.append(naloga)
        self.naslednji_id += 1

    def izbrisi_nalogo(self, id):
        for naloga in self.seznam_nalog:
            if naloga.id == id:
                self.seznam_nalog.remove(naloga)
                break
            



