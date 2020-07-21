import json

class Naloga():
    def __init__(self, id, tekst, datum=None , ura=None, prioriteta=None):
        self.tekst = tekst
        self.datum = datum
        self.ura = ura
        self.opravljeno = False
        self.prioriteta = prioriteta
        self.id = id
    
    def v_seznam(self):
        slovar = {
            'tekst': self.tekst,
            'datum': self.datum,
            'ura': self.ura,
            'opravljeno': self.opravljeno,
            'prioriteta': self.prioriteta,
            'id': self.id
        }
        return slovar



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
    
    def v_seznam(self):
        nov = []
        for naloga in self.seznam_nalog:
            nov.append(naloga.v_seznam())
        slovar = {
            'ime': self.ime,
            'naslednji_id': self.naslednji_id,
            'seznam_nalog': nov
            }
        return slovar



class Uporabnik():
    def __init__(self, ime, geslo):
        self.seznam_projektov = []
        self.ime = ime
        self.zasifrirano_geslo = geslo
    
    def shrani(self, ime_datoteke):
        nov = []
        for projekt in self.seznam_projektov:
            nov.append(projekt.v_seznam())
        slovar = {
            'ime': self.ime,
            'zasifrirano_geslo': self.zasifrirano_geslo,
            'seznam_projektov': nov
        }
        with open(ime_datoteke, 'w',encoding="utf-8") as datoteka:
            json.dump(slovar, datoteka, ensure_ascii=False, indent=4)


    def nov_projekt(self, ime):
        for projekt in self.seznam_projektov:
            if projekt.ime == ime:
                return 'error'   
        projekt = Projekt(ime)
        self.seznam_projektov.append(projekt)

    def izbrisi_projekt(self, ime):
        for projekt in self.seznam_projektov:
            if projekt.ime == ime:
                self.seznam_projektov.remove(projekt)
                break    
    
    @classmethod
    def nalozi_stanje(cls, ime_datoteke):
        with open(ime_datoteke, encoding='utf-8') as datoteka:
            slovar = json.load(datoteka)
        ime = slovar['ime']
        zasifrirano_geslo = slovar['geslo']
        uporabnik = cls(ime, zasifrirano_geslo)
        nov = []
        for pr_slovar in slovar['seznam_projektov']:
            

            

        





u = Uporabnik("Špela", "Sc.1003067")
u.nov_projekt("Tenis")
u.seznam_projektov[0].nova_naloga("Timi", [2020,7,21], 16, 5)
print(u.shrani("test.json"))